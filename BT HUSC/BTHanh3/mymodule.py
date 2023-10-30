#1
def arange(S):
    chu_thuong = ""
    chu_nthuong = ""
    for i in range(len(S)):
        if S[i] >= 'a' and S[i] <= 'z':
            chu_thuong = chu_thuong + S[i]
        else:
            chu_nthuong = chu_nthuong + S[i]
    chu = chu_thuong + chu_nthuong
    return chu
            
#2
def mix(S1,S2):
    S3 = ""
    length_s2check = len(S2) - len(S1)
    length_s1check = len(S1) - len(S2)
    for i in range(len(S1)):
        S3 = S3 + (S1[i] + S2[len(S2)-1-i])
    if length_s2check > 0:
        for i in range(length_s2check):
            S3 = S3 + S2[length_s2check-i-1]
    return S3

#3
def count_occurences(S1,S2):
    count = 0
    S1 = S1.lower()
    S2 = S2.lower()
    for i in range(len(S2)):
        for j in range(len(S1)):
            if S2[i] == S1[j] :
                count = count + 1
    if count == 0:
        return -1
    return count

#4
def sum_average(S):
    sum = 0
    count = 0
    for i in range(len(S)):
        if S[i] >= '0' and S[i] <= "9":
            sum = sum + int(S[i])
            count = count + 1
    try:
        avg = sum / count
    except:
        return "No digit"
    return "Tong: {}\nTrung binh cong: {}".format(sum,avg)
#5
def las_position(S1,S2):
    count = 0
    check = False

    for i in range(len(S2)):
        for j in range(len(S1)):
            if S2[i] == S1[j] :
                count = j
                check = True

    if check == False:
        return -1
    return count
# print(las_position("a","aaaA"))
#6
def concatenate(L1,L2):
    L3 = []
    length = len(L2) - len(L1)
    for i in range(len(L1)):
        try:
            L3.append(L1[i] + L2[i])
        except:
            L3.append(L1[i])
    if length > 0:
        for i in range(len(L2)-length,len(L2)):
            L3.append(L2[i])
    return L3
# L1 = ["H", "na", "i", "H", '18 years old']
# L2 = ["is", "me", "s", "ao"]
# print(concatenate(L1,L2))
#7
def add_new(L,item,new_item):
    pass
#8
def multiply_maxtrix(M1,M2):
    m3 = []
    for i in range(len(M1)):
        m3.append([]) 
    value = 0
    for i in range(len(M1)):
        for j in range(len(M2[0])):
            for h in range(len(M2)):
                value = value + (M1[i][h]* M2[h][j])
                # print(value)
            # print(value)
            m3[i].append(value)
            value = 0
    return m3
# M1 = [[1, 0, 0], [1, 1, 0]]
# M2 = [[1, 1, 0, 0], [0, 0, 1, 0], [1, 1, 0, 1]]
# print(multiply_maxtrix(M1,M2))
