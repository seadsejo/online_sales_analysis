from product_manager import ProductManager
from product import Product
from cart import Cart
import random

def main():
    manager = ProductManager()

    manager.add_product(Product("PC", 1400.00, 7))
    manager.add_product(Product("Laptop", 1020.60, 10))
    manager.add_product(Product("Headphones", 24.99, 15))
    manager.add_product(Product("4K Monitor", 999.99, 9))
    manager.add_product(Product("External HDD", 150.00, 5)) 
    
    print(manager.product_removal("Headphones"))
    
    print("\nDisplaying available products: ")
    manager.display_all_products()
    
    total = manager.total_inventory_value()
    print(f"\nTotal inventory value is: {total:.2f}$\n")


    cart = Cart()
    products = manager.products
    for _ in range(3):
        product = random.choice(products)
        max_quantity = min(product.quantity, 3)
        if max_quantity > 0:
            quantity = random.randint(1, max_quantity)
            cart.add_to_cart(product, quantity)

    print("\n*** Cart Status ***\n")
    cart.display_cart()
    
    cart_total = cart.calculate_total()
    print(f"\nTotal cart value: {cart_total:.2f}$")

if __name__ == "__main__":
    main()