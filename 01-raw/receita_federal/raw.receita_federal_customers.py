# Databricks notebook source
# DBTITLE 1,Setup
# Install Dependencies and Setup Framework
%pip install -r ../../00-framework/requirements.txt --quiet

import sys
sys.path.append('../../00-framework')
from data_framework import DataFramework
fw = DataFramework(dbutils, spark)

# COMMAND ----------

# DBTITLE 1,Download Files
# Set Vars
local_path = fw.configuration.local_path + "serasa/"
remote_path = fw.configuration.sftp_default_directory
files_prefix = "customers"
files_already_processed = [

]

# Download Files
fw.data_access.sftp.set_connection(
    fw.configuration.sftp_host, 
    fw.configuration.sftp_port,
    fw.configuration.sftp_user, 
    fw.configuration.sftp_private_key)
downloaded_files = fw.data_access.sftp.download_many(local_path, remote_path, files_prefix, files_already_processed)

# Print Results
fw.data_access.dbfs.print(downloaded_files)

