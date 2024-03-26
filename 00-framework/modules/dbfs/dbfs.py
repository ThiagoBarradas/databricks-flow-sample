# dbfs.py

class Dbfs:
    def __init__(self, dbutils, spark, configuration):
        """Constructor Method"""
        self.spark = spark
        self.dbutils = dbutils
        self.configuration = configuration
   
    def read_csv_from_dbfs(self, path, delimiter = ";", infer_schema = "false"):
        """Read a file from databricks file system"""
        fullpath = self.configuration.local_path_protocol + path
        dataframe = (self.spark.read
                    .option("header", "true")
                    .option("inferSchema", infer_schema)
                    .option("delimiter", delimiter).csv(fullpath))
        return dataframe
    
    def list(self, path):
        """Files in a dir"""
        fullpath = self.configuration.local_path_protocol + path
        files = []
        listed_files = self.dbutils.fs.ls(fullpath)
        for file in listed_files:
            file_path = file.path
            files.append(file_path.split("/")[-1])
        return files

    def print(self, files):
        """Print Results"""
        print("# Files #")
        if len(files) == 0:
            print("- <no files>")
        for file in files:
            print("+ " + file)