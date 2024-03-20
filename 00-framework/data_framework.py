# data_framework.py

import os
from dotenv import load_dotenv
from data_quality import DataQuality
from data_reader import DataReader
from data_writer import DataWriter
from configuration import Configuration

class DataFramework:
    def __init__(self, dbutils):
        """Constructor Method"""
        self.configuration = Configuration(dbutils);
        self.data_quality = DataQuality(self.configuration)
        self.data_reader = DataReader(self.configuration)
        self.data_writer = DataWriter(self.configuration)
        