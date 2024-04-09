# spark.py

class Spark:
    def __init__(self, spark, configuration):
        """Constructor Method"""
        self.spark = spark
        self.configuration = configuration
        self.setup_bigquery()
        spark.catalog.setCurrentCatalog(configuration.catalog)

    def setup_bigquery(self):
        spark.conf.set("credentials", self.configuration.bigquery_credentials)
        spark.conf.set("spark.hadoop.google.cloud.auth.service.account.enable", self.configuration.bigquery_enable)
        spark.conf.set("spark.hadoop.fs.gs.auth.service.account.email", self.configuration.bigquery_email)
        spark.conf.set("park.hadoop.fs.gs.project.id", self.configuration.bigquery_project_id)
        spark.conf.set("spark.hadoop.fs.gs.auth.service.account.private.key", self.configuration.bigquery_private_key)
        spark.conf.set("spark.hadoop.fs.gs.auth.service.account.private.key.id", self.configuration.bigquery_private_key_id)

    def read_from_spark_table(self, table):
        """Read a table from databricks spark source"""
        dataframe = (self.spark.read
                .format('delta')
                .table(table))
        print("read_from_spark_table > " + table + " > finish!")
        return dataframe
    
    def write_to_spark_table(self, dataframe, table, mode = "overwrite"):
        """
        Write a dataframe into databricks spark table. 
        mode "overwirte" or "append"
        """
        (dataframe.write
            .format("delta")
            .option("overwriteSchema", "true")
            .option("mergeSchema", "true")
            .mode(mode)
            .saveAsTable(name=table))
        print("write_to_spark_table > " + table + " > finish!")      

    def rename_columns(self, dataframe, columns_map):
        """Rename columns from dataframe"""
        for column_map in columns_map:
            dataframe = dataframe.withColumnRenamed(column_map[0], column_map[1])
        return dataframe
