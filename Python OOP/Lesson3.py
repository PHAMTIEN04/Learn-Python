# CLASS METHOD AND STATIC METHOD

class Car:
    tax = 1  # Class variable - represents the tax rate

    def __init__(self, brand, model, y_m, price):
        self.brand = brand
        self.model = model
        self.y_m = y_m
        self.price = price

    def get_value(self):
        # Calculating the total price including tax
        total_price = self.price + (self.price * (Car.tax / 100))  # Accessing class variable using <Class Name>.variable_name
        return total_price

    @classmethod
    def set_tax(cls):
        cls.tax = 1.5  # Class method - sets the tax rate to 1.5

    @staticmethod
    def add(x, y):
        return x + y  # Static method - adds two numbers

    @staticmethod
    def sub(x, y):
        return x - y  # Static method - subtracts two numbers


car1 = Car("BMW", "Bavaria", 1933, 1000)  # Creating a Car object

Car.set_tax()  # Calling the class method to set the tax rate to 1.5
print(Car.tax)  # Output: 1.5 (the updated tax rate)

print(f"Car {car1.brand} price is: {int(car1.get_value())} $")  # Calculating and printing the total price of car1 including tax

x = 10
y = 20
print(car1.add(x, y))  # Output: 30 (calling the static method add() on car1 object)
print(car1.sub(x, y))  # Output: -10 (calling the static method sub() on car1 object)

# *Class Method (Method of class):
# A class method is a method defined within a class and associated with that class, rather than an instance of the class' concrete object.
# To define a class method in Python, we use the @classmethod equippment before the method's declaration.
# The class method can access the properties of the class through its first parameter, commonly called "cls" (short for class). Through this parameter, we can access both class variables and other class methods.
# An important advantage of the class method is the ability to use it to create different instances of the class through the appropriate constructors.

# *Static Method (Static Method):
# A static method is a method of the class that does not access the properties or methods of the class through any special parameters (like "self" or "cls").
# To define a static method in Python, we use the @staticmethod equippment before the method's declaration.
# Static methods need no special parameters and cannot access class variables or class methods. It is often used when not related to the class information but still within the scope of the class.
# A common use of static methods is to create utility functions without creating a class object.