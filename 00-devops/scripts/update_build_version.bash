#!/bin/bash

echo "### UPDATE VERSION NUMBER ###"
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
echo "message=$message"
echo "branch=$branch"
echo "branch_name=$branch_name"
echo "build_number=$build_number"
echo "current_counter=$current_counter
echo ""

if [[ "$message" =~ "hotfix/" ]];
then 
    echo "##vso[task.setvariable variable=IsHotfix;isOutput=true]true"
    echo "##vso[task.setvariable variable=PreviousPrefix;isOutput=true]hotfix"
else
    echo "##vso[task.setvariable variable=IsHotfix;isOutput=true]false"
    echo "##vso[task.setvariable variable=PreviousPrefix;isOutput=true]release"
fi
if [[ "$branch" =~ "/hotfix/" ]] ||
   [[ "$branch" =~ "/release/" ]]; 
then
  echo "Generate Preview Release Version"
  echo "Version: $branch_name"
  echo "         ${branch_name}-preview.$current_counter"
  echo "##vso[build.updatebuildnumber]${branch_name}-preview.$current_counter"
  echo "##vso[task.setvariable variable=PureVersion;isOutput=true]$branch_name"
elif [[ "$branch" =~ "/tags/" ]];
then
  echo "Generate Release Version"
  echo "Version: $branch_name"
  echo "##vso[build.updatebuildnumber]$branch_name"
  echo "##vso[task.setvariable variable=SonarMasterWhenTag;isOutput=true]sonar.branch.name=main"
  echo "##vso[task.setvariable variable=PureVersion;isOutput=true]$branch_name"
else
  echo "Generate Development Version"
  echo "##vso[build.updatebuildnumber]${build_number}-develop"
  echo "Version: ${build_number}-develop"
fi
