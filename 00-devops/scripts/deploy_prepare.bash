#!/bin/bash

echo "### DEPLOY PREPARE - DATABRICKS CLI & DEPENDENCIES ###"
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
echo "databricks_host=$databricks_host"                    # $(DATABRICKS_HOST)
echo "databricks_client_id=$databricks_client_id"          # $(DATABRICKS_CLIENT_ID)
echo "databricks_client_secret=$databricks_client_secret"  # $(DATABRICKS_CLIENT_SECRET)
echo "databricks_account_id=$databricks_account_id"        # $(DATABRICKS_ACCOUNT_ID)
echo "profile_workspace=$profile_workspace"                # workspace
echo "profile_jobs=$profile_jobs"                          # jobs 
echo ""

echo "Configuring profiles for workspace and jobs operations..."
curl -fsSL https://raw.githubusercontent.com/databricks/setup-cli/main/install.sh | sh
pip install wheel
> ~/.databrickscfg
echo "[${profile_workspace}]" >> ~/.databrickscfg
echo "host          = $databricks_host" >> ~/.databrickscfg
echo "client_id     = $databricks_client_id" >> ~/.databrickscfg
echo "client_secret = $databricks_client_secret" >> ~/.databrickscfg
echo "" >> ~/.databrickscfg
echo "[${profile_jobs}]" >> ~/.databrickscfg
echo "host          = $databricks_host" >> ~/.databrickscfg
echo "client_id     = $databricks_client_id" >> ~/.databrickscfg
echo "client_secret = $databricks_client_secret" >> ~/.databrickscfg
echo "account_id    = $databricks_account_id" >> ~/.databrickscfg
cat ~/.databrickscfg
databricks auth profiles