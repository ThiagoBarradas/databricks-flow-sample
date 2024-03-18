# DataFramework.py
from DataQuality import DataQuality
from DataReader import DataReader
from DataWriter import DataWriter

class DataFramework:
    def __init__(self):
        """Constructor Method"""
        self.type = 'DataFramework'
        self.dataQuality = DataQuality()
        self.dataReader = DataReader()
        self.dataWriter = DataWriter()

    def getType(self):
        """Print type"""
        print(self.type)