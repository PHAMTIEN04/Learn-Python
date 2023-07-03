def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def rutgon(a, b):
    gtc = gcd(a, b)
    ts_rg = a // gtc
    ms_rg = b // gtc
    return "{}/{}".format(ts_rg, ms_rg) if gtc != 1 else ""


class Operator_overloading:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    
    def __add__(self, other):
        ts = ((self.tu * other.mau) + (other.tu * self.mau))
        ms = (self.mau * other.mau)
        return Operator_overloading(ts, ms)
    
    def __sub__(self, other):
        ts = ((self.tu * other.mau) - (other.tu * self.mau))
        ms = (self.mau * other.mau)
        return Operator_overloading(ts, ms)
    
    def __mul__(self, other):
        ts = self.tu * other.tu
        ms = other.mau * self.mau
        return Operator_overloading(ts, ms)
    
    def __truediv__(self, other):
        ts = self.tu * other.mau
        ms = self.mau * other.tu
        return Operator_overloading(ts, ms)


o1 = Operator_overloading(1, 2)
o2 = Operator_overloading(3, 4)

result_add = o1 + o2
result_add_rutgon = rutgon(result_add.tu, result_add.mau)
print(o1.tu, "/", o1.mau, " + ", o2.tu, "/", o2.mau, " = ", result_add.tu, "/", result_add.mau, sep="",end="")
if result_add_rutgon:
    print(" =", result_add_rutgon)
else:
    print()

result_sub = o1 - o2
result_sub_rutgon = rutgon(result_sub.tu, result_sub.mau)
print(o1.tu, "/", o1.mau, " - ", o2.tu, "/", o2.mau, " = ", result_sub.tu, "/", result_sub.mau, sep="",end="")
if result_sub_rutgon:
    print(" =", result_sub_rutgon)
else:
    print()

result_mul = o1 * o2
result_mul_rutgon = rutgon(result_mul.tu, result_mul.mau)
print(o1.tu, "/", o1.mau, " * ", o2.tu, "/", o2.mau, " = ", result_mul.tu, "/", result_mul.mau,sep="", end="")
if result_mul_rutgon:
    print(" =", result_mul_rutgon)
else:
    print()

result_div = o1 / o2
result_div_rutgon = rutgon(result_div.tu, result_div.mau)
print(o1.tu, "/", o1.mau, " / ", o2.tu, "/", o2.mau, " = ", result_div.tu, "/", result_div.mau,sep="", end="")
if result_div_rutgon:
    print(" =", result_div_rutgon)
else:
    print()
