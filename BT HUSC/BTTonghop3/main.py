from abc import abstractmethod 
import os
class ThuVien:
    def __init__(self,mtl,tennxb,sbph):
        self.mtl = mtl
        self.tennxb = tennxb
        self.sbph = sbph
    
    @abstractmethod
    def hienthi(self):
        print("Ma tai lieu:",self.mtl)
        print("Ten nha xuat ban:",self.tennxb)
        print("So ban phat hanh:",self.sbph)
    
    @abstractmethod
    def getloai(self):
        pass
    
    
class Sach(ThuVien):
    def __init__(self, mtl, tennxb, sbph,ttg,st):
        super().__init__(mtl, tennxb, sbph)
        self.ttg = ttg
        self.st = st
    
    def hienthi(self):
        print("**Sach**")
        super().hienthi()
        print("Ten tac gia:",self.ttg)
        print("So trang:",self.st)
        
    def getloai(self):
        return "Sach"
        
class TapChi(ThuVien):
    def __init__(self, mtl, tennxb, sbph,sph,tph):
        super().__init__(mtl, tennxb, sbph)
        self.sph = sph
        self.tph = tph
        
    def hienthi(self):
        print("**Tap Chi**")
        super().hienthi()
        print("So phat hanh",self.sph)
        print("Thang phat hanh",self.tph)        
        
    def getloai(self):
        return "TapChi"
    
class Bao(ThuVien):
    def __init__(self, mtl, tennxb, sbph,nph):
        super().__init__(mtl, tennxb, sbph)
        self.nph = nph
        
    def hienthi(self):
        print("**Bao**")
        super().hienthi()
        print("Thang phat hanh:",self.nph)

    def getloai(self):
        return "Bao"
        
class QLTaiLieu:
    ql = []
        
    def themtailieu(self):
        print("**Them Tai Lieu**")
        print("1.Sach")
        print("2.Tap Chi")
        print("3.Bao")
        choose = int(input("Chon: "))
        if choose == 1:
            mtl = str(input("Nhap ma tai lieu: "))
            tnxb = str(input("Nhap ten nha xuat ban: "))
            sbph = str(input("Nhap so ban phat hanh: "))
            ttg = str(input("Nhap ten tac gia: "))
            st = str(input("Nhap so trang: "))
            self.ql.append(Sach(mtl,tnxb,sbph,ttg,st))
        if choose == 2:
            mtl = str(input("Nhap ma tai lieu: "))
            tnxb = str(input("Nhap ten nha xuat ban: "))
            sbph = str(input("Nhap so ban phat hanh: "))
            sph = str(input("Nhap so phat hanh: "))
            tph = str(input("Nhap thang phat hanh: "))
            self.ql.append(TapChi(mtl,tnxb,sbph,sph,tph))
        if choose == 3:
            mtl = str(input("Nhap ma tai lieu: "))
            tnxb = str(input("Nhap ten nha xuat ban: "))
            sbph = str(input("Nhap so ban phat hanh: "))
            nph = str(input("Nhap ngay phat hanh: "))
            self.ql.append(Bao(mtl,tnxb,sbph,nph))
    
    def hienthitailieu(self):
        for data in self.ql:
            data.hienthi()
    
    def xoatailieu(self):
        print("**Xoa Tai Lieu**")
        mtl = str(input("Nhap ma tai lieu: "))
        for data in self.ql:
            if data.mtl == mtl:
                self.ql.remove(data)
    def timkiemtailieu(self):
        print("**Tim Kiem Tai Lieu**")
        loai = str(input("Nhap loai tai lieu: "))
        for data in self.ql:
            if data.getloai() == loai:
                data.hienthi()
    
    def menu(self):
        while True:
            print("**MENU**")
            print("1.Them tai lieu")
            print("2.Xoa tai lieu")
            print("3.Hien thi tai lieu")
            print("4.Tim kiem tai lieu")
            print("0.Thoat")
            choose = int(input("Chon: "))
            if choose == 1:
                self.themtailieu()
            if choose == 2:
                self.xoatailieu()
            if choose == 3:
                self.hienthitailieu()
            if choose == 4:
                self.timkiemtailieu()
            if choose == 0:
                break
        
    


ql = QLTaiLieu()
ql.menu()