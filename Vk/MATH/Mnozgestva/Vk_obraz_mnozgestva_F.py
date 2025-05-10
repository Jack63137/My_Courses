def fu(a):
    return a**5+1

mas = list(map(int,input().split()))
new_mas =[]
for i in mas:
    new_mas.append(fu(i))
print(*sorted(new_mas))