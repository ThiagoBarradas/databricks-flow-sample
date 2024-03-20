# Databricks notebook source
# DBTITLE 1,Setup
# MAGIC %pip install -r ../../00-framework/requirements.txt
# MAGIC
# MAGIC import sys
# MAGIC sys.path.append('../../00-framework')
# MAGIC
# MAGIC if 'dbutils' not in locals():
# MAGIC     dbutils = None

# COMMAND ----------

# DBTITLE 1,Main Code
from data_processor import DataProcessor

ignored_files = [ 
    "1.csv"
]

processor = DataProcessor(dbutils)

downloaded_files = processor.data_reader.read_files_from_sftp(
    processor.configuration.local_path,
    processor.configuration.sftp_default_directory,
    processor.configuration.sftp_host, 
    processor.configuration.sftp_port,
    processor.configuration.sftp_user, 
    processor.configuration.sftp_private_key,
    ignored_files    
)

print("# Downloaded Files #")
for file in downloaded_files:
    print("- " + file)
