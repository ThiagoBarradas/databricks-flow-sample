# sftp.py

import pysftp, paramiko, io
from urllib.parse import urlparse
import os

class Sftp:
    def __init__(self):
        """Constructor Method"""
    
    def set_connection(self, hostname, port, username, private_key):
        """Set connection parameters"""
        # Set connection object to None (initial value)
        self.connection = None
        self.hostname = hostname
        self.username = username
        self.private_key = private_key
        self.port = port
        self.cnopts = pysftp.CnOpts()
        self.cnopts.hostkeys = None   

    def connect(self):
        """Connects to the sftp server and returns the sftp connection object"""
        try:
            private_key_file_object = io.StringIO(self.private_key.replace("\\n","\n"))
            private_key = paramiko.RSAKey.from_private_key(private_key_file_object)
            # Get the sftp connection object
            self.connection = pysftp.Connection(
                host=self.hostname, 
                username=self.username, 
                private_key=private_key, 
                port=self.port,
                cnopts=self.cnopts
            )
            print(f"Connected to {self.hostname} as {self.username}.")
        except Exception as err:
            print(f"Error to connect to {self.hostname} as {self.username}.")
            raise Exception(err)

    def disconnect(self):
        """Closes the sftp connection"""
        self.connection.close()
        print(f"Disconnected from host {self.hostname}")
            
    def list(self, remote_path, prefix = None, ignored_files = []):
        """lists all the files and directories in the specified path excluding pointed names and returns them"""
        try:
            self.connect()
            for obj in self.connection.listdir(remote_path):
                if obj not in ignored_files and (prefix == None or obj.startswith(prefix)):
                    yield obj
        except Exception as err:
            raise Exception(err)
        finally:
            self.disconnect()
                
    def download(self, local_path, remote_path, file):
        """Download file"""
        try:
            if not os.path.exists(local_path):
                os.makedirs(local_path)
            if os.path.isfile(file):
                os.remove(file)
            self.connect()
            self.connection.get(remote_path + file, local_path + file)  
        except Exception as err:
            raise Exception(err)
        finally:
            self.disconnect()

    def download_many(self, local_path, remote_path, prefix = None, ignored_files = []):
        """Download many files"""
        downloaded_files = []
        try:
            self.connect()
            files = self.list(remote_path, prefix, ignored_files)
            for file in files:
                self.download(local_path, remote_path, file)  
                downloaded_files.append(file)
            return downloaded_files
        except Exception as err:
            raise Exception(err)
        finally:
            self.disconnect()     