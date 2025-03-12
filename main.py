from product_manager import ProductManager
from product import Product


manager = ProductManager()

manager.add_product(Product("PC", 1400.00, 12))
manager.add_product(Product("Laptop", 1020.60, 9))
manager.add_product(Product("Headphones", 24.99, 17))
manager.add_product(Product("4K Monitor", 999.99, 20))

#print("Displaying available products: ")
#manager.display_all_products()

#total = manager.total_inventory_value()
#print(f"\nTotal inventory value is: {total:.2f}$\n")

print(manager.product_removal("Headphones"))