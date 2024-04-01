#!/bin/bash

echo "### BUILD ###"
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
echo "local_path=$local_path"     # $(Build.Repository.LocalPath)
echo "work_dir=$work_dir"         # $(System.DefaultWorkingDirectory)
echo ""

mkdir artifact
ls $local_path
cp -r $local_path/* $work_dir/artifact
echo "### reading env files.."
find "$work_dir/artifact" -name "*.env" -print0 | while read -d $'\0' file
do
  echo "# $file"
  IFS=$'\n'
  for line in $(cat $file)
  do
    var_name=$(echo "$line" | cut -d "=" -f 1)
    echo ">> line: $line"
    echo ">>> var_name: $var_name"
    sed -i~ "/^$var_name=/s/=.*/=#{$var_name}#/" $file
  done
done
rm -rf $work_dir/artifact/artifact
find $work_dir/artifact -name "*.env~" -delete