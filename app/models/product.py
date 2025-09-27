

class Product:
    
    def __init__(self, code: str, name: str, price: float, currency: str = "EUR"):
        self.code = code        
        self.name = name        
        self.price = price      
        self.currency = currency