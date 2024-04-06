import unittest, xmlrunner, sys
sys.path.append('../../00-framework')

from setup_framework import SetupFramework
setup_framework = SetupFramework(None)

from tests.mocks.dbutils_mock import DbutilsMock
from configuration import Configuration

class ConfigurationTests(unittest.TestCase):
    def test_get_secret(self):
		    # arrange
        vault = "databricks-dev-vault"
        secret_values = {}
        secret_values["secret-1"] = "123"
        dbutils_mock = DbutilsMock(vault, secret_values)
        configuration = Configuration(dbutils_mock)

        # act 
        secret1 = configuration.get_secret("secret-1")
        empty = configuration.get_secret("empty")

        # assert
        self.assertTrue(secret1 == "123")
        self.assertTrue(empty == "")