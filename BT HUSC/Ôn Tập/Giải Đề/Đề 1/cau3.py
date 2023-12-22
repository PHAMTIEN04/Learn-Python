class HOADON:
    def __init__(self,mkh,ht,dc,csc,csm):
        self.mkh = mkh
        self.ht = ht
        self.dc= dc
        self.csc = csc
        self.csm = csm
    
    def getmkh(self):
        return self.mkh
    
    def sldsd(self):
        return self.csm - self.csc
    
    def hienthi(self):
        print("Ma khach hang:",self.mkh)
        print("Ho ten:",self.ht)
        print("Dia chi:",self.dc)
        print("Luong dien tieu thu:",self.sldsd())
        
    def __gt__(self,s):
        return self.sldsd() > s.sldsd()
    
h1 = HOADON("T","T","T",100,3200)
h2 = HOADON("A","A","A",100,300)

if h1 > h2:
    print("So Luong Dien H1 > H2")
else:
    print("So Luong Dien H2 >= H1")