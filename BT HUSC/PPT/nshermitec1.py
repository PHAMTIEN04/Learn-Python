# Nội suy Hermite cấp 1
import pandas as pd
from fractions import Fraction

def decimal_to_fraction(value):
    return str(Fraction(value).limit_denominator())

x = [-2,0,2,]
p_x = [2,3,4]
p_x1 = [4,5,6]
size = len(p_x) + len(p_x1)
x_new = []
p_new = []

check = 0
for i in range(1,size+1):
    x_new.append(x[check])
    p_new.append(p_x[check])
    if(i%2==0): check+=1


data = {
  "X": x_new,
  "P(x)": p_new
}
   
i = 0
j = 1
k = 0
cnt = 0
arr_c = []
m_p = []
while True:
    if(k == 0 and p_new[j] - p_new[i] == 0):
        value = p_x1[cnt]
        cnt+=1
    else:
        value = (p_new[j] - p_new[i])/(x_new[j+k] - x_new[i])
    if value == -0.0:
        value = 0
    arr_c.append(value)
    
    if j+1 == len(p_new):
        p_new = arr_c
        arr_c = []
        for i in range(0, size):
            try:
                if isinstance(value, float):
                    m_p.append(decimal_to_fraction(p_new[i]))
                else:
                    m_p.append(p_new[i])
            except IndexError:
                m_p.insert(0,"-")
        i = -1
        j = 0
        k += 1
        data[f"SP{k}"] = m_p
        m_p = []
        
    if len(p_new) == 1: 
        break
    i+=1
    j+=1


df = pd.DataFrame(data)

print(df)