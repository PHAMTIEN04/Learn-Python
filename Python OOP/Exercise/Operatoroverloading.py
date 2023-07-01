
class Operator_overloading:
    def __init__(self,name,pay) :
        self.name = name
        self.pay = pay
    
    def __add__(self,other):
        return self.pay + other.pay
    def __sub__(self,other):
        return self.pay - other.pay
    def __mul__(self,other):
        return self.pay * other.pay
    def __div__(self,other):
        return self.pay / other.pay
o1 = Operator_overloading("Trump",1000)
o2 = Operator_overloading("Biden",2000)

print(o1 + o2)
print(o1 - o2)
print(o1 * o2)
print(o1.__div__(o2))
