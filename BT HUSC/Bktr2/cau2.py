class KHACHHANG:
    def __init__(self,mkh = "",ht="",dc="",csc = 0,csm=0) :
        self.mkh = mkh
        self.ht = ht
        self.dc = dc
        self.csc = csc 
        self.csm = csm
    
    def getmkh(self):
        return self.mkh
    
    def sld(self):
        ldtt = self.csm - self.csc
        return ldtt
    
    def ttd(self):
        if self.sld() >= 0 and self.sld() <= 50:
            return int(self.sld()) * 1.678
        if self.sld() >= 51 and self.sld() <= 100:
            return int(self.sld()) * 1.734
        if self.sld() >= 101 and self.sld() <= 200:
            return int(self.sld()) * 2.014
        if self.sld() >= 201 and self.sld() <= 300:
            return int(self.sld()) * 2.536
        if self.sld() >= 301 and self.sld() <= 400:
            return int(self.sld()) * 2.834
        if self.sld() >= 401 :
            return int(self.sld()) * 2.927
    def hienthi(self):
        print("Ma Khach Hang:",self.mkh)
        print("Ho Ten:",self.ht)
        print("Dia Chi:",self.dc)
        print("Chi So Cu:",self.csc)
        print("Chi So Moi:",self.csm)
        print("So Luong Dien Tieu Thu:",self.sld())
        
        
    def nhap(self):
        if self.mkh == "" and self.ht=="" and self.dc=="" and self.csc == 0 and  self.csm==0:
            self.mkh = str(input("Nhap Ma Khach Hang: "))
            self.ht = str(input("Nhap Ho Ten: "))
            self.dc = str(input("Nhap Dia Chi: "))
            self.csc = int(input("Nhap Chi So Cu: "))
            self.csm = int(input("Nhap Chi So Moi: "))
    

    