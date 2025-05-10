n,maxDig = map(int,input().split())
mas = [0]*n*2
total_combinations = (maxDig+1) ** (n*2)

for _ in range(total_combinations):
    if sum(mas[:n])==sum(mas[n:]):
        print(" ".join(map(str, mas)))

    current_pos_idx = n*2 - 1
    while current_pos_idx >= 0:
        if mas[current_pos_idx] < maxDig:
            mas[current_pos_idx] += 1
            break  
        else:
            
            mas[current_pos_idx] = 0
            current_pos_idx -= 1