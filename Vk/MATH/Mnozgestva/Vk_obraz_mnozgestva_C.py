try:
    mas1 = list(map(int,input().split()))
except:
    mas1 = None
try:
    mas2 = list(map(int,input().split()))
except:
    mas2 = None
mas_fin =[]
if mas1 and mas2:
    for i in mas1:
        if i not in mas2 and i not in mas_fin:
            mas_fin.append(i)
    if mas_fin:
        print(*sorted(mas_fin))
    else:
        print("EMPTY")
else:
    if mas1:
        print(*mas1)
    else:
        print("EMPTY")