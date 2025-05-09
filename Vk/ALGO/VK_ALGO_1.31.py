mass_val = int(input())
mass = list(map(int,input().split()))
left = 0
mass_new = []
mass_null = []
while left != mass_val:
    if mass[left] !=0:
        mass_new.append(mass[left])
    left = left+1
while len(mass_new) != mass_val:
    mass_new.append(0)

print(*mass_new)