#configuration.py

import os
from dotenv import load_dotenv

class Configuration:
    def __init__(self, dbutils):
        """Constructor Method"""
        self.utils = dbutils
        self.env_file = ".env"
        if (self.utils is not None):
            self.env_file = ".env.dev"
        
        self.load_env()
       
        self.environment = self.get_env_var("ENVIRONMENT")
        self.vault = self.get_env_var("KEY_VAULT_NAME")

        self.local_path = self.get_env_var("LOCAL_PATH")
        self.sftp_default_directory = self.get_env_var("SFTP_DEFAULT_DIRECTORY")
        self.sftp_host = self.get_env_var("SFTP_HOST")
        self.sftp_port = int(self.get_env_var("SFTP_PORT"))
        self.sftp_user = self.get_env_var("SFTP_USER")
        self.sftp_private_key = self.get_secret("databricks-sftp-private-key")

        print("ENVIRONMENT: " + self.environment)

    def get_secret(self, key):
        try:
            if (self.utils is not None):
                return self.utils.secrets.get(scope=self.vault, key=key)
            else:
                return self.get_env_var(key)
        except:
            return ""
    
    def get_env_var(self, key):
        try:
            return os.getenv(key)
        except:
            return ""
    
    def load_env(self):
        """Load env vars"""
        load_dotenv(self.env_file)