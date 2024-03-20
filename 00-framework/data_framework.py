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
        self.load_env(".env")
        self.dbutils = dbutils
        self.key_vault_name = self.get_secret("KEY_VAULT_NAME")
        print("ENVIRONMENT: " + self.get_env_var("ENVIRONMENT"))
        print("KEY_VAULT_NAME: " + self.get_secret("KEY_VAULT_NAME"))
        self.data_quality = DataQuality()
        self.data_reader = DataReader()
        self.data_writer = DataWriter()
        print("Environment: " + self.get_env_var("ENVIRONMENT"))

    def get_secret(self, key):
        if (self.dbutils is not None):
            return self.dbutils.secrets.get(scope=self.key_vault_name, key=key)
        else:
            return self.get_env_var(key)
    
    def get_env_var(self, key):
        return os.getenv(key)
    
    def load_env(self, file):
        """Load env vars"""
        load_dotenv(file)