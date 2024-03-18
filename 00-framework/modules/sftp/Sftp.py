# sftp_client.py

import pysftp, paramiko, io
from urllib.parse import urlparse
import os

class Sftp:
    def __init__(self, hostname, username, private_key, port=22):
        """Constructor Method"""
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
            private_key_file_object = io.StringIO(self.private_key)
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
            
    def list_excluding(self, remote_path, excluding):
        """lists all the files and directories in the specified path excluding pointed names and returns them"""
        for obj in self.connection.listdir(remote_path):
            if obj not in excluding:
                yield obj
                
    def download(self, remote_path, file, local_path):
        """download file"""
        self.connection.get(remote_path + file, local_path + file)       