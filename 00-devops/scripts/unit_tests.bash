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
export TEST_WORKSPACE_PATH=$local_path
cd $local_path
echo "Executing unit tests"
nose2 -v -c=$local_path/00-devops/unit-test-config/.unittest.cfg
mkdir $local_path/reports
mv $local_path/*.html $local_path/reports
mv $local_path/*.xml $local_path/reports
echo "##vso[task.setvariable variable=CoverageSonar;isOutput=true]sonar.python.coverage.reportPaths=${local_path}/reports/coverage.xml"