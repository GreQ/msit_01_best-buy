import store
import products

fruid_store = store.Store()

routes = [
    ["List all products in store", fruid_store.list_products],
    ["Show total amount in store", lambda: print(f"Total products in store: {products.Product.total_products}")],
    ["Make an order", lambda: print("Order functionality not implemented yet.")],
    ["Quit", lambda: exit()]
];

def show_menu():
    while True:
        print("\nMenu:")
        for i, route in enumerate(routes):
            print(f"{i + 1}. {route[0]}")
        choice = input("Enter your choice (1-4): ")
        if choice.isdigit() and 1 <= int(choice) <= len(routes):
            routes[int(choice) - 1][1]()
        else:
            print("Invalid choice. Please try again.")

def main(shop):
    # Create a store instance
    shop.add_product(products.Product("Banane", 0.35, 5))
    shop.add_product(products.Product("Zitrone", 0.8, 15))
    shop.add_product(products.Product("Apfel", 0.22, 22))
    show_menu()

    
main(fruid_store)