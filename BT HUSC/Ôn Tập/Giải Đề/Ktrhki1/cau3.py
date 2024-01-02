class Congnhan:
    def __init__(self,mcn="",ht="",bac=0,snlv=0,nkhd = {"day":0,"month":0,"year":0}):
        self.mcn = mcn
        self.ht = ht
        self.bac = bac
        self.snlv = snlv
        self.nkhd = nkhd
        
    def TienLuong(self):
        b = {
            1:300000,
            2:350000,
            3:400000
        }
        tcn = b.get(self.bac,0)
        return self.snlv * tcn
    
    def hienthi(self):
        print("Mã công nhân:",self.mcn)
        print("Họ tên:",self.ht)
        print("Bậc:",self.bac)
        print("Số ngày làm việc:",self.snlv)
        print("Ngày kí hợp động:",self.nkhd)
        print("Tiền lương:",self.TienLuong())
        
    def __gt__(self,other):
        if self.nkhd["year"] > other.nkhd["year"]:
            return True
        elif self.nkhd["year"] == other.nkhd["year"]:
            if self.nkhd["month"] > other.nkhd["month"]:
                return True
            elif self.nkhd["month"] == other.nkhd["month"]:
                if self.nkhd["day"] > other.nkhd["day"]:
                    return True
        return False
    
