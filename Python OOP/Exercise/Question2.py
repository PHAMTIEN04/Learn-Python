# ❖Question 2: Complete Employee, Worker, Manager, Director classes and write a test program.
class Employee:
    co_salary = 1.04

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
        self.pay = int(self.pay * self.co_salary)
        return self.pay


class Worker(Employee):
    co_salary = 1.05

    def __init__(self, first, last, pay):
        # Initialize Worker instance with first name, last name, and pay
        super().__init__(first, last, pay)


class Manager(Employee):
    co_salary = 1.3

    def __init__(self, first, last, pay, employees=None):
        # Initialize Manager instance with first name, last name, pay, and employees list
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        # Add an employee to the manager's employees list
        if emp not in self.employees:
            self.employees.append(emp)

    def re_emp(self, emp):
        # Remove an employee from the manager's employees list
        if emp in self.employees:
            self.employees.remove(emp)

    def print_m(self):
        # Print the names of all employees managed by the manager
        for i in self.employees:
            print("-->", i.fullname())


class Director(Employee):
    co_salary = 1.3

    def __init__(self, first, last, pay, employees=None):
        # Initialize Director instance with first name, last name, pay, and employees list
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        # Add an employee to the director's employees list
        if emp not in self.employees:
            self.employees.append(emp)

    def re_emp(self, emp):
        # Remove an employee from the director's employees list
        if emp in self.employees:
            self.employees.remove(emp)

    def print_m(self):
        # Print the names of all employees managed by the director
        for i in self.employees:
            print("-->", i.fullname())


# Create instances of the classes and test the functionality
e = Employee("Tien", "Pham", 1000)
w = Worker("Cong", "nhan", 2000)
m = Manager("Donal", "Trump", 1000, [e, w])
print(m.fullname())
m.print_m()
d = Director("Bi", "Den", 1000, [m])
print(d.fullname())
d.print_m()
