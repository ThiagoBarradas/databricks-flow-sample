# csv.py

# spark.py

class Csv:
    def __init__(self):
        """Constructor Method"""

    def read_from_spark_table(self, table):
        """Read a table from databricks spark source"""
        dataframe = (spark.read
                .format('delta')
                .table(table))
        print("write_to_spark_table > " + table + " > finish!")
        return dataframe
    
    def read_csv_from_dbfs(self, path, delimiter = ";"):
        """
        Read a file from databricks file system
        """
        dataframe = (spark.read
                    .option("header", True)
                    .option("delimiter", delimiter).csv(path))
        return dataframe

    def write_to_spark_table(self, dataframe, table, mode = "overwrite"):
        """Write a dataframe into databricks spark table"""
        (dataframe.write
            .format("delta")
            .option("overwriteSchema", "true")
            .mode(mode)
            .saveAsTable(name=table))
        print("write_to_spark_table > " + table + " > finish!")      