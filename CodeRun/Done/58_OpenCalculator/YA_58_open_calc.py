calc_set = map(int,input().split())
calc_set = set(calc_set)

number_set = []
number = int(input())
for i in str(number):
    i = int(i)
    if i not in calc_set:
        number_set.append(i)
        
print(len(set(number_set)))