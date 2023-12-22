from cau3 import HOADON

list_hd = []
list_check = []
n = int(input())
if n <= 50:
    for i in range(n):
        mkh = str(input())
        
        ht = str(input())
        dc = str(input())
        csc = int(input())
        csm = int(input())
        if mkh not in list_check:
            list_check.append(mkh)
            list_hd.append(HOADON(mkh,ht,dc,csc,csm))
        
    for i in range(len(list_hd)-1):
        for j in range(i+1,len(list_hd)):
            if list_hd[i].sldsd() > list_hd[j].sldsd():
                tmp = list_hd[i]
                list_hd[i] = list_hd[j]
                list_hd[j] = tmp
                
    ma = str(input())
    check = False
    for i in list_hd:
        if ma == i.getmkh():
            i.hienthi()
            check = True
    if check == False:
        print("Không tồn tại khách hàng này")
        
    import csv
    
    file = "hoadon.csv"
    with open(file,"+a",newline="") as file_csv:
        for i in list_hd:
            csv_writer = csv.writer(file_csv,delimiter=";")
            str_n = [i.mkh,i.ht,i.dc]
            if i.sldsd() > 100:
                csv_writer.writerow(str_n)