from abc import abstractmethod

class PTGT:
    def __init__(self,id,hsx,nsx,gb,mx):
        self.id = id
        self.hsx = hsx
        self.nsx = nsx
        self.gb = gb
        self.mx = mx
        
    @abstractmethod
    def hienthi(self):
        print("ID:",self.id)
        print("Hang san xuat:",self.hsx)
        print("Nam san xuat:",self.nsx)
        print("Gia ban:",self.gb)
        print("Mau xe:",self.mx)
        
    def getid(self):
        return self.id
    
    def gethsx(self):
        return self.hsx
    
    def getmx(self):
        return self.mx
    
    
class OTO(PTGT):
    def __init__(self, id, hsx, nsx, gb, mx,scn,kdc):
        super().__init__(id, hsx, nsx, gb, mx)
        self.scn = scn
        self.kdc = kdc 
        
    def hienthi(self):
        print("**Oto**")
        super().hienthi()
        print("So cho ngoi:",self.scn)
        print("Kieu dong co:",self.kdc)
        
class XeMay(PTGT):
    def __init__(self, id, hsx, nsx, gb, mx,cs):
        super().__init__(id, hsx, nsx, gb, mx)
        self.cs = cs
        
    def hienthi(self):
        print("**Xe May**")
        super().hienthi()
        print("Cong suat:",self.cs)
        
class XeTai(PTGT):
    def __init__(self, id, hsx, nsx, gb, mx,tt):
        super().__init__(id, hsx, nsx, gb, mx)
        self.tt = tt
        
    def hienthi(self):
        print("**Xe Tai**")
        super().hienthi()
        print("Trong tai:",self.tt)
        
class QLPTGT:
    ql = []
    
    def themphuongtien(self):
        print("**Them Phuong Tien**")
        print("1.Oto")
        print("2.Xe may")
        print("3.Xe tai")
        choose = int(input("Chon: "))
        if choose == 1:
            id = str(input("ID: "))
            hsx = str(input("Hang san xuat: "))
            nsx = int(input("Nam san xuat: "))
            gb = float(input("Gia ban: "))
            mx = str(input("Mau xe: "))
            scn = int(input("So cho ngoi: "))
            kdc = str(input("Kieu dong co: "))
            self.ql.append(OTO(id,hsx,nsx,gb,mx,scn,kdc))
        if choose == 2:
            id = str(input("ID: "))
            hsx = str(input("Hang san xuat: "))
            nsx = int(input("Nam san xuat: "))
            gb = float(input("Gia ban: "))
            mx = str(input("Mau xe: "))
            cs = int(input("Cong suat: "))
            self.ql.append(XeMay(id,hsx,nsx,gb,mx,cs))
        if choose == 3:
            id = str(input("ID: "))
            hsx = str(input("Hang san xuat: "))
            nsx = int(input("Nam san xuat: "))
            gb = float(input("Gia ban: "))
            mx = str(input("Mau xe: "))
            tt = int(input("Trong tai: "))
            self.ql.append(XeTai(id,hsx,nsx,gb,mx,tt))
            
    def hienthiphuongtien(self):
        print("**Hien Thi Thong Tin Phuong Tien**")
        check = False
        for data in self.ql:
            data.hienthi()
            check = True
        
        if check == False:
            print("Thong Tin Trong!!!")
            
    def xoaphuongtien(self):
        print("**Xoa Thong Tin Phuong Tien**")
        choose_id = str(input("ID: "))
        check = False
        print("Dang xoa!!! Vui long doi...")
        for data in self.ql:
            if data.getid() == choose_id:
                self.ql.remove(data)
                check = True
        
        if check == True:
            print("Xoa Thanh Cong!!!")
        else:
            print("Khong Ton Tai!!!")
                
    def timphuongtien(self):
        print("**Tim Kiem Phuong Tien**")
        choose_hsx = str(input("Hang san xuat: "))
        choose_mx = str(input("Mau xe: "))
        print("Dang tim kiem!!! Vui long doi...")
        check = False
        for data in self.ql:
            if data.gethsx() == choose_hsx and data.getmx() == choose_mx:
                data.hienthi()
                check = True
                
        if check == False:
            print("Khong Tim Thay!!!")
            
    def menu(self):
        while True:
            print("**Quan Ly Phuong Tien Giao Thong**")
            print("1.Them Phuong Tien")
            print("2.Hien Thi Phuong Tien")
            print("3.Xoa Phuong Tien")
            print("4.Tim Kiem Phuong Tien")
            print("0.Thoat")
            choose = int(input("Chon: "))
            if choose == 1:
                self.themphuongtien()
            if choose == 2:
                self.hienthiphuongtien()
            if choose == 3:
                self.xoaphuongtien()
            if choose == 4:
                self.timphuongtien()
            if choose == 0:
                break
            
            
ql = QLPTGT()
ql.menu()