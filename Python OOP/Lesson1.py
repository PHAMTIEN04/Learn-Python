# OBJECT-ORIENTED PROGRAMMING IN PYTHON #1: CLASS, INSTANCE, CONSTRUCTOR FUNCTION

# CLASS
class Car:
    def __init__(self, xuatxu, namradoi):  # CONSTRUCTOR
        # Constructor function (init) is called when creating a new object of the class
        self.xuat_xu = xuatxu
        self.nam_ra_doi = namradoi

    def xuat(self):  # INSTANCE METHOD
        # Instance methods are functions defined within a class that can be called on objects of that class
        # The 'self' parameter refers to the current object instance
        return self.xuat_xu

# Creating an instance of the Car class
BMW = Car("Vietnamese", 1996)

# Accessing and modifying instance variables directly
BMW.xuatxu = "Vietnamese"
BMW.namradoi = 1996

# Printing the instance variables and calling the instance method
print(BMW.xuatxu)  # Output: Vietnamese
print(BMW.namradoi)  # Output: 1996
print(BMW.xuat())  # Output: Vietnamese
