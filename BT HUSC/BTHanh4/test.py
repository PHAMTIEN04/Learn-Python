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
        