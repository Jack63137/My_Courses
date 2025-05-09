mas_len = int(input())
mas = list(map(int,input().split()))
max_ = mas[0]
for i in range(mas_len):
    if max_ < mas[i]:
        max_ = mas[i]
print(max_)


