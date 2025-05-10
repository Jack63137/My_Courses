n = int(input())
mass = list(map(int,input().split()))
target = int(input())
count =0
for m in range(1,len(mass)-1):
    if mass[m]>mass[m-1] and mass[m] > mass[m+1]:
        count = count+1
print(count)