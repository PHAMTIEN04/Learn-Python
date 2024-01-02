from cau3 import Congnhan
list_cn = []
list_mcn = []
while True:
    
    mcn = str(input("Nhập mã công nhân: "))
    
    if mcn == "":
        break
    while mcn in list_mcn:
        print("Mã công nhân đã tồn tại.Vui lòng nhập lại!!!")
        mcn = str(input("Nhập mã công nhân: "))
    ht = str(input("Nhập họ tên: "))
    bac = int(input("Nhập bậc: "))
    snlv = int(input("Nhập số ngày làm việc: "))
    c = input("Nhap ngày kí hợp đồng (dd/mm/yyyy):").split("/")
    d = int(c[0])
    m = int(c[1])
    y = int(c[2])
    nkhd = {"day":d,"month":m,"year":y}

    list_mcn.append(mcn)
    list_cn.append(Congnhan(mcn,ht,bac,snlv,nkhd))

with open("CNBac1.txt","w") as cn_file:
    for data in list_cn:
        if data.bac == 1:
            date = str(data.nkhd["day"]) + "/" + str(data.nkhd["month"]) + "/" + str(data.nkhd["year"])
            cn_file.write(",".join([str(data.mcn),str(data.ht),str(date),str(data.snlv),str(data.TienLuong())]) + "\n")
            
cn_file.close()

for i in range(0,len(list_cn)-1):
    for j in range(i+1,len(list_cn)):
        if list_cn[i] > list_cn[j]:
            tmp = list_cn[i]
            list_cn[i] = list_cn[j]
            list_cn[j] = tmp

for i in list_cn:
    i.hienthi()
