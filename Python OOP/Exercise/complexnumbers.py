class Complex:
    i = complex(0, 1)

    def __init__(self, real, fake):
        self.real = real
        self.fake = fake

    def __add__(self, other):
        r = self.real + other.real
        f = self.fake + other.fake
        return Complex(r, f)

    def __sub__(self, other):
        r = self.real - other.real
        f = self.fake - other.fake
        return Complex(r, f)

    def __mul__(self, other):
        r = (self.real * other.real) - (self.fake * other.fake)
        f = (self.real * other.fake) + (self.fake * other.real)
        return Complex(r, f)

    def __truediv__(self, other):
        conjugate = Complex(other.real, -other.fake)
        denominator = other * conjugate
        numerator = self * conjugate
        r = numerator.real / denominator.real
        f = numerator.fake / denominator.real
        return Complex(r, f)


c1 = Complex(3, 2)
c2 = Complex(1, -1)

result_add = c1 + c2
print(c1.real, " + ", c1.fake, "i = ", result_add.real, " + ", result_add.fake, "i", sep="")

result_sub = c1 - c2
print(c1.real, " + ", c1.fake, "i", " - ", c2.real, " + ", c2.fake, "i = ", result_sub.real, " + ", result_sub.fake,
      "i", sep="")

result_mul = c1 * c2
print(c1.real, " + ", c1.fake, "i", " * ", c2.real, " + ", c2.fake, "i = ", result_mul.real, " + ", result_mul.fake,
      "i", sep="")

result_div = c1 / c2
print(c1.real, " + ", c1.fake, "i", " / ", c2.real, " + ", c2.fake, "i = ", result_div.real, " + ", result_div.fake,
      "i", sep="")
