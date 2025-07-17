n = int(input())
mass = list(map(int,input().split()))
target = int(input())
in_near =mass[0]
for i in mass:
        if abs(target-i) < abs(target-in_near):
            in_near = i
print(in_near)