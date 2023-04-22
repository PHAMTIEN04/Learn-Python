x,y = map(int,input().split()) # dùng split để tách giá trị nhập vào bằng dấu cách

def location(x,y):
    if x == 0 and y == 0:
        print("The coordinate point ","(",x,", ",y,")"," lies at the origin.",sep="")
    elif x > 0 and y>0:
        print("The coordinate point ","(",x,", ",y,")"," lies in the I quandrant.",sep="")
    elif x < 0 and y > 0: 
        print("The coordinate point ","(",x,", ",y,")"," lies in the II quandrant.",sep="")
    elif x < 0 and y < 0 :
        print("The coordinate point ","(",x,", ",y,")"," lies in the III quandrant.",sep="")
    elif x > 0 and y < 0 :
        print("The coordinate point ","(",x,", ",y,")"," lies in the IV quandrant.",sep="")
        
        
location(x,y)
