# Abstractability, Encapsulation, Polymorphism
# Abstraction: Abstraction is the ability to create abstract classes and methods that describe a concept or an object in the real world. It helps to reduce complexity by focusing on essential details and hiding unnecessary details.

# Encapsulation: Encapsulation is the combining of data and the methods that operate on that data into a single unit called an object. It allows for hiding of detailed information and restricts direct access to the data, instead interacting with the object through public methods.

# Polymorphism: Polymorphism allows an object to exhibit different behaviors in different contexts. It enables the use of a common method or attribute name to work with different objects, while the behavior of the method can vary based on the specific object type.
class Employee:
    __co_salary = 1.04 # __ private, _ protected
    def __init__(self, first, last, pay):
        # Initialize Employee instance with first name, last name, and pay
        self.first = first 
        self.last = last
        self.email = first + "." + last + "@gmail.com"
        self.pay = pay
    
    def fullname(self):
        # Return the full name of the employee
        return "{} {}".format(self.first, self.last)
    
    def apply_co_salary(self):
        # Apply the coefficient to the employee's salary and update it
        self.pay = int(self.pay * 2.5)
        return self.pay
    
class Developer(Employee): # Developer inheritance Employee
    co_salary = 1.05
    def __init__(self, first, last, pay, program):
        # Initialize Developer instance by calling the parent class's __init__ method
        super().__init__(first, last, pay)
        self.program = program

class Secretary(Employee):  # Secretary inheritance Employee
    co_salary = 1.1
    def __init__(self, first, last, pay, job):
        # Initialize Secretary instance by calling the parent class's __init__ method
        super().__init__(first, last, pay)
        self.job = job

class Manager(Employee):  # Manager inheritance Employee
    co_salary = 1.5
    def __init__(self, first, last, pay, employees=None):
        # Initialize Manager instance by calling the parent class's __init__ method
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_employee(self, emp):
        # Add an employee to the manager's list of employees
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_employee(self, emp):
        # Remove an employee from the manager's list of employees
        if emp in self.employees:
            self.employees.remove(emp)
    
    def printf(self):
        # Print the full names of the manager's employees
        for emp in self.employees:
            print("-->", emp.fullname())
    
    def check_co_salary(self):
        # Apply the coefficient to the manager's salary and return it
        return self.apply_co_salary()

# Create instances of the classes
dev1 = Developer("Tien", "Pham", 500, "Python")
dev2 = Developer("Tien", "Deptrai", 600, "C++")
sec1 = Secretary("Anna", "Nguyen", 700, "Eat with manager")
m = Manager("Khoa", "Pub", 1000, [dev1, dev2, sec1])

# Add the manager instance itself as an employee
m.add_employee(m)

# Print the manager's employees' names
m.printf()

# Apply the coefficient to the manager's salary and print it
print(m.check_co_salary())
