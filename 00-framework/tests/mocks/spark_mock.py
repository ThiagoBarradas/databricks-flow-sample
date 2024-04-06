class SparkCatalogMock:
    def __init__(self):
        self.current_catalog = "default"
    
    def setCurrentCatalog(self, catalog): 
        self.catalog = catalog
         
class SparkMock:
    def __init__(self):
        self.catalog = SparkCatalogMock()