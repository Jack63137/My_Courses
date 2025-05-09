mas_val = int(input())
mas = list(map(int,input().split()))
mas_final=[]
fin =None
for i in range(mas_val):
    if mas[i]%2==0:
        mas_final.append(mas[i])
if mas_final:
    fin = mas_final[-1]

print(fin)