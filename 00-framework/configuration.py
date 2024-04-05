# configuration.py

import pathlib, glob, os
from dotenv import load_dotenv

class Configuration:
    def __init__(self, dbutils):
        """Constructor Method"""
        self.utils = dbutils
        
        self.set_app_dir()
        self.load_env()
       
        self.environment = self.get_env_var("DATABRICKS_ENVIRONMENT")
        self.vault = self.get_env_var("DATABRICKS_KEY_VAULT_NAME")
        self.local_path = self.get_env_var("DATABRICKS_LOCAL_PATH")
        self.local_path_protocol = self.get_env_var("DATABRICKS_LOCAL_PATH_PROTOCOL")
        self.catalog = self.get_env_var("DATABRICKS_CATALOG")

        print("Environment: " + self.environment)

    def get_secret(self, key):
        """Get secret from vault if configured or from os env var"""
        return self.utils.secrets.get(scope=self.vault, key=key)
    
    def get_env_var(self, key):
        """Get env var from os"""
        try:
            return os.getenv(key)
        except:
            return ""

    def set_app_dir(self):
        """Set application base dir"""
        self.app_dir = str(os.path.abspath(__file__)).replace("00-framework/configuration.py", "");
        print("App Dir: " + self.app_dir)

    def get_env_files(self):
        """Get env file path"""
        for file in pathlib.Path(self.app_dir).rglob('*.env'):
            yield str(file)

    def load_env(self):
        """Load env vars"""
        files = self.get_env_files()

        for file in files:
            load_dotenv(file)
            print("Env File: " + file)