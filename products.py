class Product:
    total_products = 0
    
    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity
        Product.total_products += quantity