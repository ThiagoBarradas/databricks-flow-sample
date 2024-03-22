# spark.py

class Spark:
    def __init__(self, spark, configuration):
        """Constructor Method"""
        self.spark = spark
        self.configuration = configuration
        spark.catalog.setCurrentCatalog(configuration.catalog)

    def read_from_spark_table(self, table):
        """Read a table from databricks spark source"""
        dataframe = (self.spark.read
                .format('delta')
                .table(table))
        print("read_from_spark_table > " + table + " > finish!")
        return dataframe
    
    def write_to_spark_table(self, dataframe, table, mode = "overwrite"):
        """Write a dataframe into databricks spark table"""
        (dataframe.write
            .format("delta")
            .option("overwriteSchema", "true")
            .mode(mode)
            .saveAsTable(name=table))
        print("write_to_spark_table > " + table + " > finish!")      

    def rename_columns(self, dataframe, columns_map):
        """Rename columns from dataframe"""
        for column_map in columns_map:
            dataframe = dataframe.withColumnRenamed(column_map[0], column_map[1])
        return dataframe
