#configuration.py

import os
from dotenv import load_dotenv

class Configuration:
    def __init__(self, dbutils):
        """Constructor Method"""
        self.utils = dbutils
        self.load_env()
       
        self.environment = self.get_env_var("ENVIRONMENT")
        self.vault = self.get_env_var("KEY_VAULT_NAME")

        self.local_path = self.get_env_var("LOCAL_PATH")
        self.local_path_protocol = self.get_env_var("LOCAL_PATH_PROTOCOL")
        self.catalog = self.get_env_var("CATALOG")
        self.sftp_default_directory = self.get_env_var("SFTP_DEFAULT_DIRECTORY")
        self.sftp_host = self.get_env_var("SFTP_HOST")
        self.sftp_port = int(self.get_env_var("SFTP_PORT"))
        self.sftp_user = self.get_env_var("SFTP_USER")
        self.sftp_private_key = self.get_secret("databricks-sftp-private-key")

        print("ENVIRONMENT: " + self.environment)

    def get_secret(self, key):
        """Get secret from vault if configured or from os env var"""
        try:
            if (self.utils is not None):
                return self.utils.secrets.get(scope=self.vault, key=key)
            else:
                return self.get_env_var(key)
        except:
            return ""
    
    def get_env_var(self, key):
        """Get env var from os"""
        try:
            return os.getenv(key)
        except:
            return ""
        
    def get_env_file_path(self):
        """Get env file path"""
        path = os.path.dirname(os.path.realpath(__file__))
        env_file = ".env"
        if (self.utils is not None):
            env_file = ".env.dev"
        return path + "/" + env_file

    def load_env(self):
        """Load env vars"""
        file_path = self.get_env_file_path()
        load_dotenv(file_path)
        print("Env File: " + file_path)