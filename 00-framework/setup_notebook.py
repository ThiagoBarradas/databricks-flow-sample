# Databricks notebook source
# DBTITLE 1,Setup Framework
import os, sys, importlib, json

print("### Setup Notebook")
print("")
dir = os.getenv("DATABRICKS_WORKSPACE_PATH")
if (dir is None):
    print("Dir is none... Updating dynamically...")
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
    
print ("[base_workspace_dir] \n> " + dir)

setup_framework_file = dir + "/00-framework/setup_framework.py"
print ("[setup_framework_file] \n> " + setup_framework_file)

with open(setup_framework_file) as f:
    code = compile(f.read(), setup_framework_file, 'exec')
    exec(code, globals(), locals())

print("")
setup_framework = SetupFramework(dir)
fw = setup_framework.get_instance(dbutils, spark)

