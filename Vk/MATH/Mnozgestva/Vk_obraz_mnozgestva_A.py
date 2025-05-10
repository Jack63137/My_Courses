try:
    mas1 = list(map(int,input().split()))
except:
    mas1 = None
try:
    mas2 = list(map(int,input().split()))
except:
    mas2 = None

if mas1 and mas2:
    mas_uni = set(mas1 + mas2)
else:
    if mas1:
        mas_uni = set(mas1)
    elif mas2:
        mas_uni = set(mas2)
    else:
        mas_uni = None
        print("EMPTY")
if mas_uni:
    print(*sorted(mas_uni))