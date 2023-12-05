class HinhTru:
    def __init__(self, chieucao=1, bankinh=1):
        self.chieucao = chieucao
        self.bankinh = bankinh

    def thetich(self):
        return 3.14 * (self.bankinh ** 2) * self.chieucao

    def dientich_bemat(self):
        return 2 * 3.14 * self.bankinh * (self.bankinh + self.chieucao)
#------------------------------
# EXAMPLE OUTPUT
#------------------------------
c = HinhTru(2, 3)
print(c.thetich())         # 56.52
print(c.dientich_bemat())   # 94.2
