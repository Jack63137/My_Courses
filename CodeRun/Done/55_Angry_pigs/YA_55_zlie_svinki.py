n = int(input())
shots =[]
for i in range(0,n):
    x,y = map(int,input().split())
    shots.append(x)
shots_set = set(shots)
print(len(shots_set))