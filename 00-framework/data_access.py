# data_access.py

from modules.sftp.sftp import Sftp
from modules.dbfs.dbfs import Dbfs
from modules.spark.spark import Spark

class DataAccess:
    def __init__(self, dbutils, spark, configuration):
        """Constructor Method"""
        self.configuration = configuration
        self.dbfs = Dbfs(dbutils, spark)
        self.spark = Spark(spark, configuration)
        self.sftp = Sftp()