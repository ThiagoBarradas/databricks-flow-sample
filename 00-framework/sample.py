%pip install -r requirements.txt

# sample.py
from data_framework import DataFramework

framework = DataFramework(dbutils)

framework.get_type()
framework.data_quality.get_type()
framework.data_reader.get_type()
framework.data_writer.get_type()