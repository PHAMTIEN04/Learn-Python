# Define a class named HOADON (invoice)
class HOADON:
    # Constructor method to initialize instance variables
    def __init__(self, mkh, ht, dc, csc, csm):
        self.mkh = mkh  # Customer code
        self.ht = ht    # Customer name
        self.dc = dc    # Customer address
        self.csc = csc  # Previous electricity consumption
        self.csm = csm  # Current electricity consumption
    
    # Getter method to retrieve customer code
    def getmkh(self):
        return self.mkh
    
    # Method to calculate and return the electricity consumption for the current billing period
    def sldsd(self):
        return self.csm - self.csc
    
    # Method to display customer information and electricity consumption details
    def hienthi(self):
        print("Ma khach hang:", self.mkh)
        print("Ho ten:", self.ht)
        print("Dia chi:", self.dc)
        print("Luong dien tieu thu:", self.sldsd())
    
    # Overloaded greater-than method to compare electricity consumption between two instances
    def __gt__(self, s):
        return self.sldsd() > s.sldsd()

# Create two instances of the HOADON class
h1 = HOADON("T", "T", "T", 100, 3200)
h2 = HOADON("A", "A", "A", 100, 300)

# Compare the instances based on electricity consumption and print the result
if h1 > h2:
    print("Electricity Consumption of H1 is greater than H2")
else:
    print("Electricity Consumption of H2 is greater than or equal to H1")
