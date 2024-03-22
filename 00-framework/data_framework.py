# data_framework.py

import os
from dotenv import load_dotenv
from data_quality import DataQuality
from data_access import DataAccess
from configuration import Configuration

class DataFramework:
    def __init__(self, dbutils, spark):
        """Constructor Method"""
        print("Starting framework...")
        self.configuration = Configuration(dbutils);
        self.data_quality = DataQuality(self.configuration)
        self.data_access = DataAccess(dbutils, spark, self.configuration)
        print("Framework loaded!")
        