from product import Product 

class ProductManager:
    def __init__(self):
        self.products = []


    def add_product(self, product):
        self.products.append(product)


    def display_all_products(self):
        if not self.products:
            print("No products available.")
        
        else:
            for product in self.products:
                print(product.display_info())


    def total_inventory_value(self):
        total_value = sum(product.price * product.quantity for product in self.products)
        return total_value
    

    def product_removal(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                return f"Product '{product_name}' has been removed"

        return f"Product '{product_name}' is not available"