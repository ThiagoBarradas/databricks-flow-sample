# DataReader.py
from modules.sftp.Sftp import Sftp

class DataReader:
    def __init__(self):
        """Constructor Method"""
        self.type = "DataReader"

    def getType(self):
        """Print type"""
        print(self.type)
