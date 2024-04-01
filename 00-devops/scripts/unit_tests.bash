#!/bin/bash

echo "### UNIT TESTS ###"
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
echo "local_path=$local_path"                      # $(Build.Repository.LocalPath)
echo "work_dir=$work_dir"                          # $(System.DefaultWorkingDirectory)
echo "pipeline_workspace=$pipeline_workspace"      # $(Pipeline.Workspace)
echo ""

echo "TODO: execute unit tests"
#echo "##vso[task.setvariable variable=OpencoverSonar;isOutput=true]sonar.cs.opencover.reportsPaths=${pipeline_workspace}/result.opencover.xml"