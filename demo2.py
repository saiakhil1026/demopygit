class Car:
    def __init__(self, model, base_price):
        """
        Initializes a Car object with model name and base price.
        """
        self.model = model
        self.base_price = base_price
        self.accessories = {}  # Stores accessories and their prices
        self.tax_rate = 0.0  # Tax rate to be set by the user

    def add_accessory(self, name, price):
        """
        Adds an accessory with its price to the car.
        """
        self.accessories[name] = price

    def calculate_tax(self):
        """
        Calculates the tax on the car's base price plus accessories.
        """
        total_price = self.base_price + sum(self.accessories.values())
        return total_price * self.tax_rate

    def total_price(self):
        """
        Calculates the total price, including taxes and accessories.
        """
        total_price = self.base_price + sum(self.accessories.values())
        tax = self.calculate_tax()
        return total_price + tax

    def show_details(self):
        """
        Displays details of the car, accessories, and final price.
        """
        print("\nCar Details:")
        print(f"  Model: {self.model}")
        print(f"  Base Price: ${self.base_price:.2f}")
        if self.accessories:
            print("  Accessories:")
            for name, price in self.accessories.items():
                print(f"    - {name}: ${price:.2f}")
        else:
            print("  Accessories: None")
        print(f"  Tax Rate: {self.tax_rate * 100:.2f}%")
        print(f"  Tax: ${self.calculate_tax():.2f}")
        print(f"  Total Price: ${self.total_price():.2f}")
