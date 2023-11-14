SANPHAM = [{'NhaSX': 'A', 'model': 1001,'Loai': 'pc'},
           {'NhaSX': 'A', 'model': 1002,'Loai': 'pc'},
           {'NhaSX': 'A', 'model': 1003,'Loai': 'pc'},
           {'NhaSX': 'A', 'model': 2003,'Loai': 'laptop'},
           {'NhaSX': 'A', 'model': 2004,'Loai': 'laptop'},
           {'NhaSX': 'A', 'model': 2005,'Loai': 'laptop'},
           {'NhaSX': 'B', 'model': 1004,'Loai': 'pc'},           
           {'NhaSX': 'B', 'model': 1005,'Loai': 'pc'},
           {'NhaSX': 'B', 'model': 3001,'Loai': 'printer'},
           {'NhaSX': 'B', 'model': 2006,'Loai': 'laptop'},           
           {'NhaSX': 'C', 'model': 3002,'Loai': 'printer'},
           {'NhaSX': 'D', 'model': 2001,'Loai': 'laptop'},
           {'NhaSX': 'D', 'model': 2002,'Loai': 'laptop'},           
           {'NhaSX': 'D', 'model': 3003,'Loai': 'printer'},
           {'NhaSX': 'D', 'model': 3004,'Loai': 'printer'},
           {'NhaSX': 'D', 'model': 3005,'Loai': 'printer'},           
           ]

LAPTOP = [{'model':2001,'TocDo':2.00,'RAM':4096,'HDD':240,'ManHinh':20.1,'Gia':3675},
          {'model':2002,'TocDo':1.73,'RAM':2048,'HDD':80,'ManHinh':17.0,'Gia':949},
          {'model':2003,'TocDo':1.80,'RAM':1024,'HDD':60,'ManHinh':15.4,'Gia':549},
          {'model':2004,'TocDo':2.00,'RAM':2048,'HDD':60,'ManHinh':13.3,'Gia':1150},
          {'model':2005,'TocDo':2.16,'RAM':2048,'HDD':120,'ManHinh':17.0,'Gia':2500},
          {'model':2006,'TocDo':2.00,'RAM':2048,'HDD':80,'ManHinh':15.4,'Gia':1700},
          ]

PC = [{'model':1001,'TocDo':2.66,'RAM':4096,'HDD':250,'Gia':2114},
      {'model':1002,'TocDo':2.10,'RAM':4096,'HDD':250,'Gia':995},
      {'model':1003,'TocDo':1.42,'RAM':2048,'HDD':80,'Gia':478},
      {'model':1004,'TocDo':2.80,'RAM':1024,'HDD':250,'Gia':649},
      {'model':1005,'TocDo':3.20,'RAM':512,'HDD':250,'Gia':630},
      ]

PRINTER = [{'model':3001,'Mau':'true','Loai':'ink-jet','Gia':99},
           {'model':3002,'Mau':'false','Loai':'laser','Gia':239},
           {'model':3003,'Mau':'true','Loai':'laser','Gia':899},
           {'model':3004,'Mau':'true','Loai':'ink-jet','Gia':120},
           {'model':3005,'Mau':'false','Loai':'laser','Gia':120},
           ]

def cau1(SANPHAM):

    list_pc = []
    list_pr = []
    list_check = []
    for i in SANPHAM:
        if i['Loai'] == 'pc':
            list_pc.append(i['NhaSX'])
        if i['Loai'] == 'printer':
            list_pr.append(i['NhaSX'])

    if 'A' in list_pr and 'A' not in list_pc:
        list_check.append('A')
    if 'B' in list_pr and 'B' not in list_pc:
        list_check.append('B')
    if 'C' in list_pr and 'C' not in list_pc:
        list_check.append('C')
    if 'D' in list_pr and 'D' not in list_pc:
        list_check.append('D')

    return list_check

print("Cau1:", cau1(SANPHAM=SANPHAM))
        
        
def cau2(PC):
    list_check = []
    for i in PC:
        if i['TocDo'] >= 2.50:
            list_check.append(i['model'])
    
    return list_check

print("Cau2:",cau2(PC=PC))

def cau3(SANPHAM,LAPTOP):
    list_model = []
    list_check = []
    result = []
    for i in LAPTOP:
        if i['HDD'] >= 125:
            list_model.append(i['model'])
            
    for i in SANPHAM:
        if i['model'] in list_model:
            list_check.append(i['NhaSX'])
            
    if 'A' in list_check:
        result.append('A')
    if 'B' in list_check:
        result.append('B')
    if 'C' in list_check:
        result.append('C')
    if 'D' in list_check:
        result.append('D')
    return result

print("Cau3:",cau3(SANPHAM=SANPHAM,LAPTOP=LAPTOP))

def cau4(SANPHAM,PC,LAPTOP,PRINTER):
    list_m_c = []
    for i in SANPHAM:
        if i['NhaSX'] == 'C':
            list_m_c.append(i['model'])
   
    list_g = []
   
    for i in PC:
        if i['model'] in list_m_c:
            list_g.append(i['Gia'])
    for i in LAPTOP:
        if i['model'] in list_m_c:
            list_g.append(i['Gia'])
    for i in PRINTER:
        if i['model'] in list_m_c:
            list_g.append(i['Gia'])
           
    return list_m_c,list_g

print("Cau4",cau4(SANPHAM=SANPHAM,PC=PC,LAPTOP=LAPTOP,PRINTER=PRINTER))

def cau5(PRINTER):
    list_md = []
    for i in PRINTER:
        if i['Loai'] == 'laser' and i['Mau'] == 'false':
            list_md.append(i['model'])
           
    return list_md

print("Cau5",cau5(PRINTER=PRINTER))

def cau6(SANPHAM):
    list_a = []
    list_b = []
    list_c = []
    list_d = []
    list_check = []
    for i in SANPHAM:
        if i['NhaSX'] == 'A' and i['Loai'] not in list_a:
            list_a.append(i['Loai'])
        if i['NhaSX'] == 'B' and i['Loai'] not in list_b:
            list_b.append(i['Loai'])
        if i['NhaSX'] == 'C' and i['Loai'] not in list_c:
            list_c.append(i['Loai'])
        if i['NhaSX'] == 'D' and i['Loai'] not in list_d:
            list_d.append(i['Loai'])
    if len(list_a) == 3:
        list_check.append('A')
    if len(list_b) == 3:
        list_check.append('B')
    if len(list_c) == 3:
        list_check.append('C')
    if len(list_d) == 3:
        list_check.append('D')
    return list_check

print("Cau6",cau6(SANPHAM=SANPHAM))

def cau7(SANPHAM):
    list_a = []
    list_b = []
    list_c = []
    list_d = []
    list_check = []
    for i in SANPHAM:
        if i['NhaSX'] == 'A' and i['Loai'] not in list_a:
            list_a.append(i['Loai'])
        if i['NhaSX'] == 'B' and i['Loai'] not in list_b:
            list_b.append(i['Loai'])
        if i['NhaSX'] == 'C' and i['Loai'] not in list_c:
            list_c.append(i['Loai'])
        if i['NhaSX'] == 'D' and i['Loai'] not in list_d:
            list_d.append(i['Loai'])
    if len(list_a) == 1 and 'pc' in list_a:
        list_check.append('A')
    if len(list_b) == 1 and 'pc' in list_b:
        list_check.append('B')
    if len(list_c) == 1 and 'pc' in list_c:
        list_check.append('C')
    if len(list_d) == 1 and 'pc' in list_d:
        list_check.append('D')
    return list_check  
   
print("Cau7",cau7(SANPHAM=SANPHAM))

def cau8(SANPHAM):
    list_a = []
    list_b = []
    list_c = []
    list_d = []
    list_check = []
    for i in SANPHAM:
        if i['NhaSX'] == 'A' and i['Loai'] not in list_a:
            list_a.append(i['Loai'])
        if i['NhaSX'] == 'B' and i['Loai'] not in list_b:
            list_b.append(i['Loai'])
        if i['NhaSX'] == 'C' and i['Loai'] not in list_c:
            list_c.append(i['Loai'])
        if i['NhaSX'] == 'D' and i['Loai'] not in list_d:
            list_d.append(i['Loai'])
    if len(list_a) == 1 and ('pc' in list_a or 'laptop' in list_a):
        list_check.append('A')
    if len(list_b) == 1 and ('pc' in list_b or 'laptop' in list_b):
        list_check.append('B')
    if len(list_c) == 1 and ('pc' in list_c or 'laptop' in list_c):
        list_check.append('C')
    if len(list_d) == 1 and ('pc' in list_d or 'laptop' in list_d):
        list_check.append('D')
    return list_check  
   
print("Cau8",cau8(SANPHAM=SANPHAM))

def cau9(SANPHAM):
    list_a = []
    list_b = []
    list_c = []
    list_d = []
    list_check = []
    for i in SANPHAM:
        if i['NhaSX'] == 'A' and i['Loai'] not in list_a:
            list_a.append(i['Loai'])
        if i['NhaSX'] == 'B' and i['Loai'] not in list_b:
            list_b.append(i['Loai'])
        if i['NhaSX'] == 'C' and i['Loai'] not in list_c:
            list_c.append(i['Loai'])
        if i['NhaSX'] == 'D' and i['Loai'] not in list_d:
            list_d.append(i['Loai'])
    if 'pc' in list_a and 'laptop' in list_a:
        list_check.append('A')
    if 'pc' in list_b and 'laptop' in list_b:
        list_check.append('B')
    if 'pc' in list_c and 'laptop' in list_c:
        list_check.append('C')
    if 'pc' in list_d and 'laptop' in list_d:
        list_check.append('D')
    return list_check  
   
print("Cau9",cau9(SANPHAM=SANPHAM))

def cau10(PC):
    list_a = [] 
    list_b = []
    list_check = []
    check = 0
    list_done = []
    for i in PC:
        if i['HDD'] not in list_a:
            list_a.append(i['HDD'])
        list_b.append(i['HDD'])
    for i in list_a:
        for j in list_b:
            if i == j:
                check = check + 1
        list_check.append(check)
        check = 0
    for i in range(len(list_a)):
        if list_check[i] >= 2:
            list_done.append(list_a[i])
    return list_done

print("Cau10",cau10(PC=PC)) 
    
def cau11(PC):
    list_n = []
    list_check = []
    for i in PC:
        list_n.append([i['model'],i['TocDo'],i['RAM']])
    
    for i in range(0,len(list_n)-1):
        for j in range(i+1,len(list_n)):
            if list_n[i][1] == list_n[j][1] and list_n[i][2] == list_n[j][2]:
                if list_n[i][0] not in list_check:
                    list_check.append(list_n[i][0])
                list_check.append(list_n[j][0])
    return list_check

print('Cau11',cau11(PC=PC))

def cau12(SANPHAM,LAPTOP,PC):
    list_a = []
    list_b = []
    list_c = []
    list_d = []
    list_a_check = []
    list_b_check = []
    list_c_check = []
    list_d_check = []
    list_a_cnt = []
    list_b_cnt = []
    list_c_cnt = []
    list_d_cnt = []
    list_done = []
    md_pc = []
    md_lt = []
    check = 0
    for i in PC:
        if i['TocDo'] >= 2.20:
            md_pc.append(i['model'])
    for i in LAPTOP:
        if i['TocDo'] >= 2.20:
            md_lt.append(i['model'])
        
    
    for i in SANPHAM:
        if i['NhaSX'] == 'A' and i['model'] in (md_pc or md_pc):
            list_a.append(i['Loai'])
            if i['Loai'] not in list_a_check:
                list_a_check.append(i['Loai'])
        if i['NhaSX'] == 'B' and i['model'] in (md_pc or md_pc):
            list_b.append(i['Loai'])
            if i['Loai'] not in list_b_check:
                list_b_check.append(i['Loai'])
        if i['NhaSX'] == 'C' and i['model'] in (md_pc or md_pc):
            list_c.append(i['Loai'])
            if i['Loai'] not in list_c_check:
                list_c_check.append(i['Loai'])
        if i['NhaSX'] == 'D' and i['model'] in (md_pc or md_pc):
            list_d.append(i['Loai'])
            if i['Loai'] not in list_d_check:
                list_d_check.append(i['Loai'])
    
    for i in list_a_check:
        for j in list_a:
            if i == j:
                check = check + 1
        list_a_cnt.append(check)
        check = 0
    
    for i in list_b_check:
        for j in list_b:
            if i == j:
                check = check + 1
        list_b_cnt.append(check)
        check = 0
    for i in list_c_check:
        for j in list_c:
            if i == j:
                check = check + 1
        list_c_cnt.append(check)
        check = 0
    for i in list_d_check:
        for j in list_d:
            if i == j:
                check = check + 1
        list_d_cnt.append(check)
        check = 0
    
    for i in range(len(list_a_check)):
        if list_a_check[i] == 'pc' or list_a_check[i] == 'laptop' and list_a_cnt[i] >= 2:
            if 'A' not in list_done:
                list_done.append('A')
    for i in range(len(list_b_check)):
        if list_b_check[i] == 'pc' or list_b_check[i] == 'laptop' and list_b_cnt[i] >= 2:
            if 'B' not in list_done:
                list_done.append('B')
    for i in range(len(list_c_check)):
        if list_c_check[i] == 'pc' or list_c_check[i] == 'laptop' and list_c_cnt[i] >= 2:
            if 'C' not in list_done:
                list_done.append('C')
    for i in range(len(list_d_check)):
        if list_d_check[i] == 'pc' or list_d_check[i] == 'laptop' and list_d_cnt[i] >= 2:
            if 'D' not in list_done:
                list_done.append('D')
    
    
    return list_done
print("Cau12",cau12(SANPHAM=SANPHAM,LAPTOP=LAPTOP,PC=PC))