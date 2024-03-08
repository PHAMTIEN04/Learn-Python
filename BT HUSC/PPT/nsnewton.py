# Nội Suy Newton
import pandas as pd
from fractions import Fraction
def decimal_to_fraction(value):
    return str(Fraction(value).limit_denominator())
x = [-1,-2,1,2]
p_x = [1,2,3,4]
size = len(p_x)


data = {
  "X": x,
  "P(x)": p_x
}

i = 0
j = 1
k = 0
arr_c = []
m_p = []
while True:
    try:
        value = (p_x[j] - p_x[i])/(x[j+k] - x[i])
        arr_c.append(value)
    
        if j+1 == len(p_x):
            p_x = arr_c
            arr_c = []
            for i in range(0, size):
                try:
                    if isinstance(value, float):
                        m_p.append(decimal_to_fraction(p_x[i]))
                    else:
                        m_p.append(p_x[i])
                except IndexError:
                    m_p.insert(0,"-")
            i = -1
            j = 0
            k += 1
            data[f"SP{k}"] = m_p
            m_p = []
        
        if len(p_x) == 1: 
            break
        i+=1
        j+=1
    except:
        print("Error!!!")
        break
        
df = pd.DataFrame(data)

print(df)