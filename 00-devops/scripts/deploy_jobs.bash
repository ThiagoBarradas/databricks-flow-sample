#!/bin/bash

echo "### DEPLOY JOBS ###"
echo ""

# get vars
for ARGUMENT in "$@"
do
  KEY=$(echo $ARGUMENT | cut -f1 -d=)
  KEY_LENGTH=${#KEY}
  VALUE="${ARGUMENT:$KEY_LENGTH+1}"
  export "$(echo $KEY | tr -d '-')"="$VALUE"
done

echo "# Vars"
echo "job_prefix=$job_prefix"
echo "job_dir=$job_dir"
echo "profile=$profile" 
echo ""

# get local jobs
> local_jobs.txt
find "$job_dir" -name "*.job.json" -print0 | while read -d $'\0' file
do
  job_name=$(jq -r '.name' $file)
  echo "$job_name" >> local_jobs.txt
done
readarray -t local_jobs < local_jobs.txt

echo "# Local Jobs"
for job in "${local_jobs[@]}"; do
  echo $job
done
echo ""

# get remote jobs
databricks jobs list --profile=$profile | tr -s ' ' > remote_jobs_raw.txt
IFS=$'\n'
for line in $(cat remote_jobs_raw.txt)
do
  job_name=$(echo "$line" | cut -d" " -f2)
  if  [[ $job_name == $job_prefix* ]]; then
    echo "$job_name" >> remote_jobs.txt
  fi
done
readarray -t remote_jobs < remote_jobs.txt

echo "# Remote Jobs"
for job in "${remote_jobs[@]}"; do
  echo $job
done
echo ""

# check actions

> jobs_to_create.txt
> jobs_to_update.txt
> jobs_to_delete.txt

for local_job in "${local_jobs[@]}"; do
  if [[ ${remote_jobs[@]} =~ $local_job ]]; then
    echo "$local_job" >> jobs_to_update.txt
  else
    echo "$local_job" >> jobs_to_create.txt
  fi
done

for remote_job in "${remote_jobs[@]}"; do
  if ! [[ ${local_jobs[@]} =~ $remote_job ]]; then
    echo "$remote_job" >> jobs_to_delete.txt
  fi
done

readarray -t jobs_to_create < jobs_to_create.txt
readarray -t jobs_to_update < jobs_to_update.txt
readarray -t jobs_to_delete < jobs_to_delete.txt

echo "# Jobs to Create"
for job in "${jobs_to_create[@]}"; do
  echo $job
done
echo ""

echo "# Jobs to Update"
for job in "${jobs_to_update[@]}"; do
  echo $job
done
echo ""

echo "# Jobs to Delete"
for job in "${jobs_to_delete[@]}"; do
  echo $job
done
echo ""

# executing actions

find "$job_dir" -name "*.job.json" -print0 | while read -d $'\0' file
do
  job_name=$(jq -r '.name' $file)
  
  if [[ ${jobs_to_create[@]} =~ $job_name ]]; then
    echo "# Creating $job_name from $file"
	  databricks jobs create --json="@$file" --profile=$profile
  else
	  job_id=$(sed -n "/$job_name/p" remote_jobs_raw.txt | cut -d" " -f1)
    echo "# Updating $job_name ($job_id) from $file"
	  jq "del(.run_as)" $file > "tmp" && mv "tmp" $file
    jq '{"new_setting": .}' < $file > "tmp" && mv "tmp" $file
	  jq ". += { \"job_id\": $job_id }" $file > "tmp" && mv "tmp" $file
	  databricks jobs update --json="@$file" --profile=$profile
  fi
done

for job_name in "${jobs_to_delete[@]}"; do
  job_id=$(sed -n "/$job_name/p" remote_jobs_raw.txt | cut -d" " -f1)
  echo "# Deleting $job_name ($job_id)"
  databricks jobs delete $job_id --profile=$profile
done
echo ""

# clean
echo "# Cleaning temp files"
rm -f local_jobs.txt
rm -f remote_jobs.txt
rm -f remote_jobs_raw.txt
rm -f jobs_to_create.txt
rm -f jobs_to_update.txt
rm -f jobs_to_delete.txt

echo "# Deploy finished!"