# data_reader.py

from modules.sftp.sftp import Sftp
from framework_base import FrameworkBase

class DataReader(FrameworkBase):
    def __init__(self):
        """Constructor Method"""
        super().__init__("data_reader")
