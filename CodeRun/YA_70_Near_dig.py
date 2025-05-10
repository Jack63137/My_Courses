n = int(input())
mass = list(map(int,input().split()))
target = int(input())
in_max =0
for i in range(0,len(mass)):
    if abs(mass[in_max]) - abs(mass[i]) <0:
        in_max = i
print(mass[in_max])