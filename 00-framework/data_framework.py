#%pip install -r requirements.txt
# data_framework.py

import os
from dotenv import load_dotenv
from framework_base import FrameworkBase
from data_quality import DataQuality
from data_reader import DataReader
from data_writer import DataWriter

class DataFramework(FrameworkBase):
    def __init__(self, dbutils):
        """Constructor Method"""
        super().__init__("data_framework")
        load_dotenv()
        self.dbutils = dbutils
        self.keyVaultName = self.get_secret("KeyVaultName")
        self.dataQuality = DataQuality()
        self.dataReader = DataReader()
        self.dataWriter = DataWriter()
        print("Environment: " + self.get_env_var("Environment"))

    def get_secret(self, key):
        if (self.dbutils is not None):
            return self.dbutils.secrets.get(scope=self.keyVaultName, key=key)
        else:
            return self.get_env_var(key)
    
    def get_env_var(self, key):
        return os.getenv(key)