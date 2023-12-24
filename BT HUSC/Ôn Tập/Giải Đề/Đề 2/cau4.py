import csv 
from cau3 import Iris
list_iris = []
with open("Iris.csv","r") as read_csv:
    csv_read = csv.reader(read_csv)
    print(csv_read)
    cnt = 0
    for i in csv_read:
        
        if cnt > 0:
            list_iris.append(Iris(float(i[0]),float(i[1]),float(i[2]),float(i[3]),str(i[4])))
        cnt = cnt + 1

X = Iris(7.1,2.8,6.4,1.6,C=None)
list_kc =[]
for data in list_iris:
    list_kc.append(X.khoangcach(data))

sort_list_kc = sorted(list_kc)
print(sort_list_kc)
list_kc = sort_list_kc[0:3]
list_h = []

for data in list_iris:
    if X.khoangcach(data) == list_kc[0] or X.khoangcach(data) == list_kc[1] or X.khoangcach(data) == list_kc[2]:
        list_h.append(data.C)
        
print(list_h)

h1 = "setosa"
h2 = "versicolor"
h3 = "virginica"

cnt_h1 = 0
cnt_h2 = 0
cnt_h3 = 0

for i in list_h:
    if i == h1:
        cnt_h1 += 1
    if i == h2:
        cnt_h2 += 1
    if i == h3:
        cnt_h3 += 1
        
if cnt_h1 > cnt_h2 and cnt_h1 > cnt_h2:
    X.setKieuhoa(h1)
if cnt_h2 > cnt_h1 and cnt_h2 > cnt_h3:
    X.setKieuhoa(h2)
if cnt_h3 > cnt_h2 and cnt_h3 > cnt_h1: 
    X.setKieuhoa(h3)
    
print(X.C)