mas_cal= int(input())
mas = list(map(int,input().split()))
f1 = mas[0]
f2 = mas[1]
for i in range(mas_cal-1):
    if abs(f1 - f2)>abs(mas[i]-mas[i+1]):
        f1 = mas[i]
        f2 = mas[i+1]
print(f1,f2)