# Databricks notebook source
# DBTITLE 1,Setup
# MAGIC %run ../../00-framework/setup_notebook

# COMMAND ----------

table = "dataplatform-nonprd.credit_open.webhook_notification_deliveries"
df = spark.read.format("bigquery").option("parentProject","dataplatform-nonprd").option("table", table).load()

df.show(3)


# COMMAND ----------

# DBTITLE 1,Download Files
# Set Vars
sftp_path = fw.configuration.get_env_var("DATABRICKS_RAW_RECEITA_FEDERAL_SFTP_DEFAULT_DIRECTORY")
sftp_host = fw.configuration.get_env_var("DATABRICKS_RAW_RECEITA_FEDERAL_SFTP_HOST")
sftp_port = int(fw.configuration.get_env_var("DATABRICKS_RAW_RECEITA_FEDERAL_SFTP_PORT"))
sftp_user = fw.configuration.get_env_var("DATABRICKS_RAW_RECEITA_FEDERAL_SFTP_USER")
sftp_private_key_secret_name = fw.configuration.get_env_var("DATABRICKS_RAW_RECEITA_FEDERAL_SFTP_PRIVATE_KEY_SECRET_NAME")
sftp_private_key = fw.configuration.get_secret(sftp_private_key_secret_name)
local_path = "receita_federal/"
files_prefix = "customers"
files_already_processed = [

]

# Download Files
fw.data_access.sftp.set_connection(
    sftp_host, 
    sftp_port,
    sftp_user, 
    sftp_private_key)
downloaded_files = fw.data_access.sftp.download_many(local_path, sftp_path, files_prefix, files_already_processed)

# Print Results
fw.data_access.dbfs.print(downloaded_files)

