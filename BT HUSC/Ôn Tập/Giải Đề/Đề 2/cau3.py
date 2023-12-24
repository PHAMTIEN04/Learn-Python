import math
class Iris:
    def __init__(self,x1,x2,x3,x4,C = None):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.x4 = x4
        self.C = C
        
    def setKieuhoa(self,C):
        self.C = C
    
    def khoangcach(self,i2):
        list_r = [self.x1,self.x2,self.x3,self.x4]
        list_r2 = [i2.x1,i2.x2,i2.x3,i2.x4]
        kc = 0
        for i in range(len(list_r)):
            kc += math.sqrt(math.pow((list_r[i] - list_r2[i]),2))
        kc = round(kc,2)
        return kc

i1 = Iris(7.1,2.8,6.4,1.6)
i2 = Iris(4,5,6,7)

print(i1.khoangcach(i2))
                
    
        