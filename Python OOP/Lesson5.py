# SPECIAL METHODS

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + last + "@gmail.com"
        self.pay = pay

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def __repr__(self):
        return f"{self.first} {self.last} {self.pay}"
    # The __repr__ method returns a string that represents the object.
    # It is used to provide a detailed and unambiguous string representation of the object.
    # In this case, it returns a formatted string with the first name, last name, and pay of the Employee object.

    def __str__(self):
        return f"{self.fullname()} - {self.email}"
    # The __str__ method returns a string that represents the object in a readable format.
    # It is used to provide a concise and user-friendly string representation of the object.
    # In this case, it returns a formatted string with the full name and email of the Employee object.

    def __add__(self, other):
        return self.pay + other.pay
    # The __add__ method defines the behavior of the '+' operator when applied to two Employee objects.
    # It returns the sum of the 'pay' attributes of the two objects.

    def __len__(self):
        return len(self.fullname())
    # The __len__ method defines the behavior of the len() function when applied to an Employee object.
    # It returns the length of the full name of the Employee object.


e1 = Employee("Tien", "Pham", 1000)
e2 = Employee("Tien", "Dep trai", 1400)

print(e1 + e2)  # Prints the sum of 'pay' attributes of e1 and e2
print(e1.fullname())  # Prints the full name of e1
print(e1.email)  # Prints the email of e1
print(repr(e1))  # Prints the string representation of e1 (using __repr__)
print(str(e1))  # Prints the string representation of e1 (using __str__)
print(len(e1))  # Prints the length of the full name of e1


import datetime

today = datetime.datetime.now()
print(str(today))  # Prints the string representation of the 'today' object
print(repr(today))  # Prints the string representation of the 'today' object
