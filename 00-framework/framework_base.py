# framework_base.py

class FrameworkBase:
    def __init__(self, type):
        """Constructor Method"""
        self.type = type

    def get_type(self):
        """Print type"""
        print(self.type)