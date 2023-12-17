from abc import abstractmethod

class CanBo:
    def __init__(self,mcb = "",ht = "",ns = 0,tdcm= "",hsl=0,snct=0):
        self.mcb = mcb
        self.ht = ht
        self.ns = ns
        self.tdcm = tdcm
        self.hsl = hsl
        self.snct = snct
        
    def nhap(self):
        if self.mcb == "" and self.ht == "" and self.ns == 0 and self.tdcm == "" and self.hsl ==0 and self.snct==0:
            self.mcb = str(input("Ma can bo: "))
            self.ht = str(input("Ho ten: "))
            self.ns = int(input("Ngay sinh: "))
            self.tdcm = str(input("Trinh do chuyen mon: "))
            self.hsl = float(input("He so luong: "))
            self.snct = int(input("So nam cong tac: "))
    
    @abstractmethod
    def TinhLuong(self):
        pass
    
    def xuat(self):
        print("Ma can bo :",self.mcb)
        print("Ho ten :",self.ht)
        print("Ngay sinh :",self.ns)
        print("Trinh do chuyen mon :",self.tdcm)
        print("He so luong :",self.hsl)
        print("So nam cong tac :",self.snct)
    
    @abstractmethod
    def getloai(self):
        pass
    
    def getmcb(self):
        return self.mcb
    
class GiangVien(CanBo):
    def __init__(self,lcb = 0,mcb="", ht="", ns=0, tdcm="", hsl=0, snct=0):
        super().__init__(mcb, ht, ns, tdcm, hsl, snct)
        self.lcb = lcb
        self.pcud = 0.4*(self.hsl * self.lcb)
        self.pctn = 50.000*self.snct
        
    def nhap(self):
        if self.lcb == 0 and self.mcb == "" and self.ht == "" and self.ns == 0 and self.tdcm == "" and self.hsl ==0 and self.snct==0:
            super().nhap()
            self.lcb = float(input("Luong co ban : "))
    
    def TinhLuong(self):
        return (self.hsl * self.lcb) + self.pcud + self.pctn
    
    def xuat(self):
        super().xuat()
        print("Luong co ban :",self.lcb)
        print("Tien Luong :",self.TinhLuong())
    
    def getloai(self):
        return "GiangVien"


class ChuyenVien(CanBo):
    def __init__(self,lcb = 0,pccb = 0,mcb="", ht="", ns=0, tdcm="", hsl=0, snct=0):
        super().__init__(mcb, ht, ns, tdcm, hsl, snct)
        self.lcb = lcb
        self.pccb = pccb
        
    def nhap(self):
        if self.lcb == 0 and self.pccb == 0 and self.mcb == "" and self.ht == "" and self.ns == 0 and self.tdcm == "" and self.hsl ==0 and self.snct==0:
            super().nhap()
            self.lcb = float(input("Luong co ban : "))
            self.pccb = float(input("Phu cap can bo : "))

    def TinhLuong(self):
        return (self.hsl * self.lcb) + self.pccb
    
    def xuat(self):
        super().xuat()
        print("Luong co ban :",self.lcb)
        print("Phu cap can bo :",self.pccb)
        print("Tien Luong :",self.TinhLuong())     
        
    def getloai(self):
        return "ChuyenVien"
    
class QLCB:
    ql = []
    n = 0
    
    
    def tkcb(self):
        print("**Giang Vien**")
        for data in self.ql:
            if data.getloai() == "GiangVien":
                data.xuat()
                
        print("**Chuyen Vien**")
        for data in self.ql:
            if data.getloai() == "ChuyenVien":
                data.xuat()
                
    def xoa(self):
        print("**Xoa Can Bo**")
        mcb = str(input("Ma can bo : "))
        for data in self.ql:
            if data.getmcb() == mcb:
                self.ql.remove(data)
                
    def menu(self):
        while True:
            print("**Quan Ly Can Bo**")
            print("1.Nhap giang vien moi")
            print("2.Nhap chuyen vien moi")
            print("3.Xoa can bo")
            print("4.Thong ke cac can bo theo ngach")
            print("5.Thoat")
            choose = int(input("Chon : "))
            if choose == 1:
                self.ql.append(GiangVien())
                self.ql[self.n].nhap()
                self.n = self.n + 1
            if choose == 2:
                self.ql.append(ChuyenVien())
                self.ql[self.n].nhap()
                self.n = self.n + 1
            if choose == 3:
                self.xoa()
            if choose == 4:
                self.tkcb()
            if choose == 5:
                break
            
ql = QLCB()
ql.menu()  