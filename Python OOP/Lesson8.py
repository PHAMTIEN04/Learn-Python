# Abstract Method
from abc import ABC, abstractmethod

class AbstractArray(ABC):
    def __init__(self, m, n):
        # Initialize the dimensions and array
        self.m = m
        self.n = n
        self.a = []

    @abstractmethod
    def input(self):
        pass

    @abstractmethod
    def output(self):
        pass

class TwoDimensionalArray(AbstractArray):
    def input(self):
        # Prompt the user to enter values for each row
        print(f"Enter {self.m} rows with {self.n} values separated by spaces:")
        for i in range(self.m):
            input_str = input(f"Row {i+1}: ")
            # Split the input values by spaces and convert them to integers
            row_values = input_str.split()
            row = [int(value) for value in row_values]
            self.a.append(row)

    def output(self):
        # Print the array elements
        for i in range(self.m):
            for j in range(self.n):
                print(self.a[i][j], end=" ")
            print("\n", end="")

# Create a TwoDimensionalArray object with dimensions 3x4
arr = TwoDimensionalArray(3, 4)

# Input values for the two-dimensional array
arr.input()

# Output the values of the two-dimensional array
arr.output()
