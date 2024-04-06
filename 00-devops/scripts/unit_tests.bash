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
echo ""

echo "Installing unit tests tools"
pip install unittest
pip install nose2
pip install nose2[coverage_plugin]
pip install nose2-html-report
export TEST_WORKSPACE_PATH=$(Build.Repository.LocalPath)
cd $(Build.Repository.LocalPath)

echo "Executing unit tests"
nose2 -v -c=$(Build.Repository.LocalPath)/00-devops/unit-test-config/.unittest.cfg

echo "##vso[task.setvariable variable=OpencoverSonar;isOutput=true]sonar.python.coverage.reportPaths=${pipeline_workspace}/coverage.xml"