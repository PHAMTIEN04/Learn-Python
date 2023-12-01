
class SANPHAM:
    model = [1001,1002,1003,2003,2004,2005,1004,1005,3001,2006,3002,2001,2002,3003,3004,3005]
    NhaSX = ['A','A','A','A','A','A','B','B','B','B','C','D','D','D','D','D']
    Loai = ['pc','pc','pc','laptop','laptop','laptop','pc','pc','printer','laptop','printer','laptop','laptop','printer','printer','printer']
    def cau1(self):
        list_r = []
        check_A = True
        check_B = True
        check_C = True
        check_D = True
        for i in range(len(self.NhaSX)):
            if self.NhaSX[i] == 'A' and self.Loai[i] == 'pc':
                check_A = False
            if self.NhaSX[i] == 'B' and self.Loai[i] == 'pc':
                check_B = False
            if self.NhaSX[i] == 'C' and self.Loai[i] == 'pc':
                check_B = False
            if self.NhaSX[i] == 'D' and self.Loai[i] == 'pc':
                check_B = False
        if check_A == True:
            list_r.append('A')
        if check_B == True:
            list_r.append('B')
        if check_C == True:
            list_r.append('C')
        if check_D == True:
            list_r.append('D')
        return list_r

class LAPTOP(SANPHAM):
    model = [2001,2002,2003,2004,2005,2006]
    TocDo = [2.00,1.73,1.80,2.00,2.16,2.00]
    RAM = [4096,2048,1024,2048,2048,2048]
    HDD = [240,80,60,60,120,80]
    ManHinh = [20.1,17.0,15.4,13.3,17.0,15.4]
    Gia = [3675,949,549,1150,2500,1700]
class PC(SANPHAM):
    model = [1001,1002,1003,1004,1005]
    TocDo = [2.66,2.10,1.42,2.80,3.20]
    RAM = [4096,4096,2048,1024,512]
    HDD = [250,250,80,250,250]
    Gia = [2114,995,478,649,630]
class PRINTER(SANPHAM):
    model = [3001,3002,3003,3004,3005]
    Mau = ["true","false","true","true","false"]
    Loai = ["ink-jet","laser","laser","ink-jet","laser"]
    Gia = [99,239,899,120,120]