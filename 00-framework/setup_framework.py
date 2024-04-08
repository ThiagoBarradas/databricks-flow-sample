# set workdir
import os, subprocess, inspect 

class SetupFramework:
    def __init__(self, dir):
        print("### Setup Framework")
        print()

        dir_test = os.getenv("TEST_WORKSPACE_PATH")
        dir = os.getenv("DATABRICKS_WORKSPACE_PATH")

        if (dir_test is not None):
            dir = dir_test
        elif (dir is None or dir == ""):
            dev_prefix = "/Workspace/Repos/development/"
            other_prefix = "/Workspace/"
            dir = os.path.dirname(os.path.realpath('__file__'))
            if (dir.startswith(dev_prefix)):
                split = dir.index('/', len(dev_prefix))
                dir = dir[0:split]
            else:
                split = dir.index('/', len(other_prefix))
                dir = dir[0:split]
        
        os.environ["DATABRICKS_WORKSPACE_PATH"] = dir;
        
        self.dir = dir;
        self.install_dependencies()
        self.append_code()               
    
    def install_dependencies(self):
        print("[installing_dependencies]")
        import subprocess, warnings
        subprocess.run(
            "pip install -r \""+ self.dir + "/00-framework/requirements.txt\" --quiet --disable-pip-version-check", 
            shell = True, 
            executable="/bin/bash")
        
        # ignore warning from lib
        from cryptography.utils import CryptographyDeprecationWarning
        warnings.filterwarnings(action='ignore', category=CryptographyDeprecationWarning)
        
    def append_code(self):
        print("[appending_code]")
        import sys
        sys.path.append(self.dir + '/00-framework')

    def get_instance(self, dbutils, spark):
        print("[loading_framework]")
        from data_framework import DataFramework
        return DataFramework(dbutils, spark)