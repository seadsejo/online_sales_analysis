from product import Product

class Cart:
    def __init__(self):
        self.cart_items = []


    def add_to_cart(self, product, quantity):
        if quantity <= product.quantity:
            self.cart_items.append({"product": product, "quantity": quantity})
            product.update_quantity(-quantity) 
        
        else:
            print(f"Not enough units for {product.name}. Available units: {product.quantity}")


    def calculate_total(self):
        total = sum(item["product"].price * item["quantity"] for item in self.cart_items)
        return total


    def display_cart(self):
        if not self.cart_items:
            print("Cart is empty.")
        
        else:
            print("Items in cart: ")
            for item in self.cart_items:
                product = item["product"]
                quantity = item["quantity"]
                print(f"{product.name}: {quantity} units, price: {product.price * quantity:.2f}$")
