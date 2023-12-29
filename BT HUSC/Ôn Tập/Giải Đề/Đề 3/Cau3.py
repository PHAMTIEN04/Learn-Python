class LO_DAT:
    def __init__(self,cd=0,cr=0,l=0):
        self.cd = cd
        self.cr = cr
        self.l = l
    
    def nhap(self):
        self.cd = int(input("Nhap chieu dai: "))
        self.cr = int(input("Nhap chieu rong: "))
        self.l = int(input("Nhap loai: "))
        
    def hienthi(self):
        print("Chieu dai:",self.cd)
        print("Chieu rong:",self.cr)
        print("Loai:",self.l)
        
    def chuvi(self):
        return (self.cd + self.cr) * 2
    
    def dientich(self):
        return self.cd * self.cr
    
class QLLD:
    ql = []
    def __init__(self,n):
        self.n = n 
    def nhap(self):
        print("**Nhap Lo Dat**")
        i = 0
        while i < self.n:
            print("Lo Dat [{}]".format(i+1))
            self.ql.append(LO_DAT())
            self.ql[i].nhap()

            i = i + 1
    
    def hienthi(self):
        print("**Hien thi Lo Dat**")
        j = 0
        for i in self.ql:
            print("Lo Dat [{}]".format(j+1))
            i.hienthi()
            j = j + 1
    
    def cvln(self):
        print("**Lo Dat Chu Vi Lon Nhat")
        max = self.ql[0]
        for i in range(1,len(self.ql)):
            if max.chuvi() < self.ql[i].chuvi():
                max = self.ql[i]
        for i in self.ql:
            if max.chuvi() == i.chuvi():
                i.hienthi()
    
    def cvnn(self):
        print("**Lo Dat Chu Vi Nho Nhat")
        max = self.ql[0]
        for i in range(1,len(self.ql)):
            if max.chuvi() > self.ql[i].chuvi():
                max = self.ql[i]
        for i in self.ql:
            if max.chuvi() == i.chuvi():
                i.hienthi()
    
    def sapxep(self):
        print("**Sap Xep Lo Dat Theo Thu Tu Tang Dan Dien Tich**")
        for i in range(0,len(self.ql)-1):
            for j in range(i+1,len(self.ql)):
                if self.ql[i].dientich() > self.ql[j].dientich():
                    tmp = self.ql[i]
                    self.ql[i] = self.ql[j]
                    self.ql[j] = tmp
        self.hienthi()
    
    def lietke(self):
        print("**Liet Ke**")
        for i in self.ql:
            if i.l == 1:
                gt = 30
            if i.l == 2:
                gt = 27
            if i.l == 3:
                gt = 24 
            if (i.dientich() >= 100 and i.dientich() <= 150) and (i.dientich()*gt < 3500):
                i.hienthi()    
    
    def menu(self):
        while True:
            print("**QUAN LY LO DAT**")
            print("1.Nhap Lo Dat")
            print("2.Hien thi Lo Dat")
            print("3.Tim kiem Lo Dat chu vi lon nhat")
            print("4.Tim kiem Lo Dat chu vi nho nhat")
            print("5.Sap xep Lo Dat tang dan theo dien tich")
            print("6.Liet Ke")
            print("0.Thoat")
            choose = int(input("Chon: "))
            if choose == 1:
                self.nhap()
            if choose == 2:
                self.hienthi()
            if choose == 3:
                self.cvln()
            if choose == 4:
                self.cvnn()
            if choose == 5:
                self.sapxep()
            if choose == 6:
                self.lietke()
            if choose == 0:
                break
    
ql = QLLD(3)
ql.menu()