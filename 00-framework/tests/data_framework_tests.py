import unittest, xmlrunner, sys
sys.path.append('../../00-framework')

from setup_framework import SetupFramework
setup_framework = SetupFramework(None)

from data_framework import DataFramework
from tests.mocks.dbutils_mock import DbutilsMock
from tests.mocks.spark_mock import SparkMock

class DataFrameworkTests(unittest.TestCase):
    def test_new_framework(self):
        # arrange
        secret_values = {}
        dbutils_mock = DbutilsMock("databricks-dev-vault", secret_values)
        spark_mock = SparkMock()

        # act 
        fw = DataFramework(dbutils_mock, spark_mock)

        # assert
        self.assertTrue(fw.data_access is not None)
        self.assertTrue(fw.data_quality is not None)
        self.assertTrue(fw.configuration is not None)
            