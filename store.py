

import products


class Store:

    def __init__(self):
        self.products = []

    #add a product to the store's product list
    def add_product(self, product):
        if type(product) is not products.Product:
            print("Invalid product type.")
        elif product in self.products:
            print(f"{product.name} is already in the store's product list.")
        else:
            self.products.append(product)

    #remove a product from the store's product list
    def remove_product(self, product):
        self.products.remove(product)

    def list_products(self):
        print ("\n-----\nProducts in store:")
        num = 0
        for product in self.products:
            num += 1
            print(f"{num}. {product.name} - ${product.price} - Quantity: {product.quantity}")
        print ("-----")