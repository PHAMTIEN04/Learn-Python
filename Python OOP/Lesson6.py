# Property, Getter, Setter, Deleter
# Property: Property allows you to define getter, setter and deleter methods to manage accessing and assigning values ​​to an object's properties.

# Getter: Getter is a method used to get the value of an attribute. It allows you to access and read the value of a property without directly accessing the property's variable.

# Setter: Setter is a method used to assign values ​​to properties. It allows you to inspect and process data before assigning new values ​​to properties.

# Deleter: Deleter is a method used to delete an attribute. It allows you to perform delete operations or clean up associated data when an attribute is deleted.

class Car:
    """
    Class representing a car.
    """

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def fullname(self):
        return f"{self.brand} {self.model}"

    @property
    def fullname(self):
        """
        Getter method to retrieve the full name of the car (brand + model).
        """
        return f"{self.brand} {self.model}"

    @fullname.setter
    def fullname(self, full_name):
        """
        Setter method to update the brand and model of the car based on a full name.
        """
        brand, model = full_name.split(" ")
        self.brand = brand
        self.model = model

    @fullname.deleter
    def fullname(self):
        """
        Deleter method to reset the brand and model of the car.
        """
        self.brand = None
        self.model = None


# Creating an instance of Car
car1 = Car("Vinfast", "Vietnamese")

# Accessing the fullname property using the getter
print(car1.fullname)  # Output: Vinfast Vietnamese

# Updating the fullname property using the setter
car1.fullname = "BMW USA"
print(car1.fullname)  # Output: BMW USA

# Accessing the brand and model attributes directly
print(car1.brand)  # Output: BMW
print(car1.model)  # Output: USA

# Deleting the fullname property using the deleter
del car1.fullname
print(car1.fullname)  # Output: None