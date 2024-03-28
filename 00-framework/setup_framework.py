# Databricks notebook source
# DBTITLE 1,Setup Framework
# Install Dependencies and Setup Framework
%pip install -r ../../00-framework/requirements.txt --quiet

import sys, warnings, os
sys.path.append('../../00-framework')

from cryptography.utils import CryptographyDeprecationWarning
warnings.filterwarnings(action='ignore', category=CryptographyDeprecationWarning)

from data_framework import DataFramework
fw = DataFramework(dbutils, spark)
