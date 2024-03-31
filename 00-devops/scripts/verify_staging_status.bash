#!/bin/bash

echo "### VERIFY STAGING STATUS ###"
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
echo "message=$message"            # $(Build.SourceVersionMessage)
echo "branch=$branch"              # $(Build.SourceBranch)
echo "branch_name=$branch_name"    # $(Build.SourceBranchName)
echo "build_number=$build_number"  # $(Build.BuildNumber)
echo ""

STAGING_URL="https://dev.azure.com/$(organization)/$(System.TeamProject)/_apis/build/status/$(System.DefinitionId)?branchName=$(UpdateBuildVersionTask.PreviousPrefix)/$(Build.BuildNumber)&stageName=DeployPackage"
STAGING_RESULT=$`curl --silent $STAGING_URL`
echo "URL: $STAGING_URL" 
echo "RESULT: $STAGING_RESULT"
SUCCEEDED=$`echo $STAGING_RESULT | grep -P 'succeeded' -o | head -n 1`
if [[ "$STAGING_RESULT" =~ "succeeded" ]];
then
  echo "$PREVIOUS_PREFIX branch is ok!"
else
  echo "$PREVIOUS_PREFIX branch is not ok!"
  exit 1
fi