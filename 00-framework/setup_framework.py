# Databricks notebook source
# DBTITLE 1,Setup Framework
# set workdir
import os, subprocess

workspace_dir = os.getenv("ENVIRONMENT_CLUSTER")
if (workspace_dir is None):
    workspace_dir = "../.."
else:
    workspace_dir = "/Workspace/" + workspace_dir
    os.chdir(workspace_dir)
    print("Startup Workdir:")
    print(os.getcwd())
    print("")

# install dependencies
subprocess.run(
    "pip install -r \""+ workspace_dir + "/00-framework/requirements.txt\" --quiet --disable-pip-version-check", 
    shell = True, 
    executable="/bin/bash")

# append all code
import sys, warnings
sys.path.append(workspace_dir + '/00-framework')

# ignore warning from lib
from cryptography.utils import CryptographyDeprecationWarning
warnings.filterwarnings(action='ignore', category=CryptographyDeprecationWarning)

# load framework
from data_framework import DataFramework
fw = DataFramework(dbutils, spark)
