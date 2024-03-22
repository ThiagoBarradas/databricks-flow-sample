# dbfs.py

class Dbfs:
    def __init__(self, dbutils, spark):
        """Constructor Method"""
        self.spark = spark
        self.dbutils = dbutils
   
    def read_csv_from_dbfs(self, path, delimiter = ";"):
        """Read a file from databricks file system"""
        dataframe = (self.spark.read
                    .option("header", True)
                    .option("delimiter", delimiter).csv(path))
        return dataframe
    
    def list(self, path):
        """Files in a dir"""
        files = []
        listed_files = self.dbutils.fs.ls(path)
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