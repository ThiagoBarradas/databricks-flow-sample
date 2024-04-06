class DbutilsSecretsMock:
    def __init__(self, scope, secret_values):
        self.scope = scope
        self.secret_values = secret_values
    
    def get(self, scope, key): 
        if (scope == self.scope):
            try:
                return self.secret_values[key]
            except KeyError:
                return ""    
        else:
            return ""
    
class DbutilsMock:
     def __init__(self, scope, secret_values):
        self.secrets = DbutilsSecretsMock(scope, secret_values)