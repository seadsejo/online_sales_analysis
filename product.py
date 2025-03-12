class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


    def display_info(self):
        return f"Name: {self.name}, Price: {self.price:.2f}$, Quantity: {self.quantity}"


    def update_quantity(self, amount):
        self.quantity += amount
       
        if self.quantity < 0:
            self.quantity = 0 
            print(f"Quantity for {self.name} cannot be negative. Setting quantity to 0.")