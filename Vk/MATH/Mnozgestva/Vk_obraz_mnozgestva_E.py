from datetime import datetime
n = int(input())
mas = [None] * n  # создаем список из n элементов
for i in range(n):
    name,check,date = input().split()
    mas[i] = str(name),float(check), str(date)

sorted_mas_name = sorted(mas, key=lambda x: x[0])
sorted_mas_check = sorted(mas, key=lambda x: x[1])
sorted_mas_date = sorted(mas, key=lambda x: datetime.strptime(x[2], "%d.%m.%Y"))


for i in range(n):
    print(*sorted_mas_name[i])
print("#")
for i in range(n):
    print(*sorted_mas_check[i])
print("#")
for i in range(n):
    print(*sorted_mas_date[i])