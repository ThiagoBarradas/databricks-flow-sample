# data_processor.py

from framework_base import FrameworkBase

class DataProcessor(FrameworkBase):
    def __init__(self, type):
        """Constructor Method"""
        super().__init__(type)

    def read(self):
        """Read abstract method"""
        print("read: Not implemented")
        raise NotImplementedError("read: Subclasses should implment this!")
    
    def process(self):
        """Process abstract method"""
        print("process: Method not implemented")
        raise NotImplementedError("process: Subclasses should implment this!")
    
    def write(self):
        """Write abstract method"""
        print("write: Method not implemented")
        raise NotImplementedError("write: Subclasses should implment this!")
    
    def verify(self):
        """Verify abstract method"""
        print("verify: Method not implemented")
        raise NotImplementedError("verify: Subclasses should implment this!")