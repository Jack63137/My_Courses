mass_val = int(input())
mass = list(map(int,input().split()))
mass_del = int(input())
left = 0
mass_new = []
mass_null = []
while left != mass_val:
    if mass[left] != mass_del:
        mass_new.append(mass[left])
    left = left+1

print(*mass_new)