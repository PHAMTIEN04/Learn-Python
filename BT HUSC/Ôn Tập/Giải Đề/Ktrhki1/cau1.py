D = "Truong Dai hoc Khoa hoc Dai hoc Hue"
D = D.split()
list_c = []
cnt = 0
for i in range(len(D)):
    if D[i] not in list_c:
        list_c.append(D[i])
        for j in range(len(D)):
            if D[i] == D[j]:
                cnt = cnt + 1
        pw = (cnt/len(D))*100
        if i == len(D)-1:
            print("p({}): {}%".format(D[i],pw))
        else:
            print("p({}): {}%".format(D[i],pw),end = ", ")
        cnt = 0
    