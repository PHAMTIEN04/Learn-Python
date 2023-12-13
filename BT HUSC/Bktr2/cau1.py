import math 
def Sigmoid(x):
    return 1/(1+(math.e**(-x)))

data = input().split()
data = [int(x) for x in data]

for x in data:
    print(round(Sigmoid(x),3),end=" ")