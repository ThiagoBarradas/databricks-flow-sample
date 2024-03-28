# Databricks notebook source
# DBTITLE 1,Setup
# MAGIC %run ../../00-framework/setup_framework

# COMMAND ----------

# DBTITLE 1,Parse Files to Bronze
# Set Vars
local_path = "receita_federal/"
columns = [ 
    [ "Index", "index" ],
    [ "Customer Id", "customer_id"], 
    [ "First Name", "first_name"], 
    [ "Last Name", "last_name"],
    [ "Company", "company"],
    [ "City", "city"],
    [ "Country", "country"],
    [ "Phone 1", "phone_1"],
    [ "Phone 2", "phone_2"],
    [ "Email", "email"],
    [ "Subscription Date", "subscription_date" ],
    [ "Website", "website" ]
]

files = fw.data_access.dbfs.list(local_path)
fw.data_access.dbfs.print(files)

for file in files:
    df = fw.data_access.dbfs.read_csv_from_dbfs(local_path + file, ",")
    df = fw.data_access.spark.rename_columns(df, columns)
    fw.data_access.spark.write_to_spark_table(df, "bronze.receital_federal_customers", "overwrite")



