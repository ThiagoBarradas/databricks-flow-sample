# Databricks notebook source
# MAGIC %run ../../00-framework/setup_notebook

# COMMAND ----------

import os

os.environ["GOOGLE_CLOUD_PROJECT"] = "dataplatform-nonprd"
os.environ["GCP_PROJECT"] = "dataplatform-nonprd"
os.environ["GCP_PROJECT_ID"] = "dataplatform-nonprd"

df = spark.read.format("bigquery").option("table", "dataplatform-nonprd.credit_open.webhook_notification_deliveries").load()

df.show(3)

