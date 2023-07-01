# OBJECT-ORIENTED PROGRAMMING IN PYTHON #2: CLASS VARIABLES

class Car:
    tax = 1  # Class Variable
    # To use a variable outside of a specific scope, you can add an underscore '_' before the variable name.
    # Ex: _tax = value

    def __init__(self, brand, model, y_m, price):
        # Instance Variables
        self.brand = brand
        self.model = model
        self.y_m = y_m
        self.price = price
        self.tax += 1

    def get_value(self):
        # Calculating the total price including tax
        total_price = self.price + (self.price * (Car.tax / 100))  # Accessing class variable using <Class Name>.variable_name
        return total_price


# Creating car instances
car1 = Car("Vinfast", "Vietnamese", 1998, 1000)
car2 = Car("BMW", "Bavaria", 1993, 700)

# Printing the prices of the cars
print(f"Car {car1.brand} price is: {int(car1.get_value())} $")
print(f"Car {car2.brand} price is: {int(car2.get_value())} $")

# Accessing class variable tax
print(car1.tax)
print(car2.tax)
