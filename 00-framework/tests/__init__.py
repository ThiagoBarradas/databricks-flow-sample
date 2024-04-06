import sys, os, unittest

print("Init tests...")

workspace_path = os.getenv("TEST_WORKSPACE_PATH")
sys.path.append(workspace_path + "/00-framework")

from setup_framework import SetupFramework
setup_framework = SetupFramework(None)



