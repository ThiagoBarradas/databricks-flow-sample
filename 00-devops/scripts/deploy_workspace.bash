#!/bin/bash

echo "### DEPLOY WORKSPACE ###"
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
echo "workspace_path=$workspace_path"   # $(DATABRICKS_WORKSPACE_PATH)
echo "import_dir=$import_dir"           # $(System.DefaultWorkingDirectory)/$(project_name)Staging
echo "profile=$profile"                 # workspace
echo ""

mkdir temp
mv "${import_dir}/05-jobs/*" temp
rm -rf "${import_dir}/05-jobs"
rm -rf "${import_dir}/.git"
rm -rf "${import_dir}/00-devops"
rm -rf "${import_dir}/README.md"
rm -rf "${import_dir}/.gitignore"

echo "# Cleaning up workspace..."
databricks workspace delete $workspace_path --recursive --profile=$profile
echo "# Importing new files to workspace..."
databricks workspace import-dir $import_dir $workspace_path --profile=$profile

mkdir ${import_dir}/05-jobs
mv temp/* "${import_dir}/05-jobs"
rm -rf temp

echo "# Deploy finished!"