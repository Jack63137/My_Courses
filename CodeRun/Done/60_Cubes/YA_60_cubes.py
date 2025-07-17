n_anya, n_borya = map(int, input().split())
set_anya = set()
set_borya = set()
for i in range(n_anya):
    x = int(input())
    set_anya.add(x)

for i in range(n_borya):
    x = int(input())
    set_borya.add(x)

set_obshee = set_anya & set_borya
set_anya_unique = set_anya - set_borya
set_borya_unique = set_borya - set_anya

print(len(set_obshee))
print(*sorted(set_obshee))
print(len(set_anya_unique))
print(*sorted(set_anya_unique))
print(len(set_borya_unique))
print(*sorted(set_borya_unique))