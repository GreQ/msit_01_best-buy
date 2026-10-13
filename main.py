import store
import products

fruid_store = store.Store()
active_options = "main_options"

routes = [
    ["List all products in store", fruid_store.list_products],
    ["Show total amount in store",  lambda: print(f"Total products in store: {products.Product.total_products}")],
    ["Make an order", lambda: show_order_options(fruid_store)],
    ["Quit", lambda: exit()]
];

def place_order(product_name, quantity):
    for product in fruid_store.products:
        if product.name == product_name:
            if product.quantity >= quantity:
                product.quantity -= quantity
                products.Product.total_products -= quantity
                print(f"Order placed for {quantity} {product_name}(s).")
            else:
                print(f"Not enough {product_name} in stock. Available quantity: {product.quantity}.")
            return
    print(f"{product_name} not found in the store.")    

def show_main_options():
    active_options = "main_options"
    while active_options == "main_options":
        print("\n***** Store Menu *****")
        for i, route in enumerate(routes):
            print(f"{i + 1}. {route[0]}")
        choice = input("Enter your choice (1-4): ")
        if choice.isdigit() and 1 <= int(choice) <= len(routes):
            routes[int(choice) - 1][1]()
        else:
            print("Invalid choice. Please try again.")

def show_order_options(shop):
    active_options = "order_options"
    while active_options == "order_options":
        print("\nWhen you want to finish order just hit return.")
        shop.list_products()
        choice = input("Which product # do you want?")
        if choice.isdigit() and int(choice) <= len(shop.products):
            product = shop.products[int(choice) - 1]
            quantity = input(f"How many '{product.name}s' do you want to order? ")
            if quantity.isdigit() and int(quantity) > 0:
                place_order(product.name, int(quantity))
            else:
                print("Invalid quantity. Please enter a positive number.")
                show_main_options()
        elif choice == "":
            print("Order finished.")
            show_main_options()
        else:
            print("Invalid choice. Please try again.")
            show_main_options()

def main(shop):
    # Create a store instance
    shop.add_product(products.Product("Banana", 0.35, 5))
    shop.add_product(products.Product("Lemon", 0.8, 15))
    shop.add_product(products.Product("Apple", 0.22, 22))
    show_main_options()

    
main(fruid_store)