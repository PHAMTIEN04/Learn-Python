n = int(input())
p = 0
h = 0
if n >= 60:
    p = n//60
    n = n - (p*60)
if p >= 60:
    h = p//60
    p = p - (h*60)
 
if len(str(h)) >=2:
    print(f"{h}:",end="")
else:
    print(f"0{h}:",end="")
if len(str(p)) >=2:
    print(f"{p}:",end="")
else:
    print(f"0{p}:",end="")
if len(str(n)) >=2:
    print(f"{n}",end="")
else:
    print(f"0{n}",end="")