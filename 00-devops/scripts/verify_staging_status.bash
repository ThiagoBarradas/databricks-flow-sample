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
echo "org=$org"                           # $(organization)
echo "team=$team"                         # $(System.TeamProject)
echo "definition_id=$definition_id"       # $(System.DefinitionId)
echo "previous_prefix=$previous_prefix"   # $(UpdateBuildVersionTask.PreviousPrefix)
echo "stage=$stage"                       # DeployStaging
echo "build_number=$build_number"         # $(Build.BuildNumber)
echo ""

STAGING_URL="https://dev.azure.com/$org/$team/_apis/build/status/${definition_id}?branchName=${previous_prefix}/${build_number}&stageName=#stage"
STAGING_RESULT=$`curl --silent $STAGING_URL`
echo "URL: $STAGING_URL" 
echo "RESULT: $STAGING_RESULT"
SUCCEEDED=$`echo $STAGING_RESULT | grep -P 'succeeded' -o | head -n 1`
if [[ "$STAGING_RESULT" =~ "succeeded" ]];
then
  echo "$previous_prefix branch is ok!"
else
  echo "$previous_prefix branch is not ok!"
  exit 1
fi