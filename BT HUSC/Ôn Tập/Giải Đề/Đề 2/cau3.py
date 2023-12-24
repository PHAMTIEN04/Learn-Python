import math

# Define a class named Iris
class Iris:
    # Constructor method to initialize instance variables
    def __init__(self, x1, x2, x3, x4, C=None):
        self.x1 = x1  # Feature 1
        self.x2 = x2  # Feature 2
        self.x3 = x3  # Feature 3
        self.x4 = x4  # Feature 4
        self.C = C    # Class label (default is None)
        
    # Method to set the class label (C) for an instance
    def setKieuhoa(self, C):
        self.C = C
    
    # Method to calculate the Euclidean distance between two instances
    def khoangcach(self, i2):
        list_r = [self.x1, self.x2, self.x3, self.x4]          # Feature values of the current instance
        list_r2 = [i2.x1, i2.x2, i2.x3, i2.x4]                 # Feature values of the other instance
        kc = 0
        
        # Calculate the Euclidean distance for each feature and accumulate the result
        for i in range(len(list_r)):
            kc += math.sqrt(math.pow((list_r[i] - list_r2[i]), 2))
        
        # Round the calculated distance to two decimal places
        kc = round(kc, 2)
        return kc

# Create two instances of the Iris class
i1 = Iris(7.1, 2.8, 6.4, 1.6)
i2 = Iris(4, 5, 6, 7)

# Calculate and print the Euclidean distance between the two instances
print(i1.khoangcach(i2))
