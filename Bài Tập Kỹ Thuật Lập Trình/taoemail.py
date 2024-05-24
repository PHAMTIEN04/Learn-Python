st = str(input())

if(len(st) <= 50):
    st = st.lower().split(" ")
    new_st = [] 
    for i in st:
        if i != '':
            new_st.append(i)
    if(len(new_st) == 1):
        print(new_st[0],end="")
    if(len(new_st) > 1):
        s = ""
        for i in range(len(new_st)-1):
            c = list(new_st[i])
            s += c[0]
        print(s+new_st[len(new_st)-1],end="")
    print("@husc.edu.vn")