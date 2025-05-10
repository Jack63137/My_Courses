coins,pirate_a,pirate_b,pirate_c = map(float,input().split())
flag = False
for a in range(int(coins)):
    if a >= (coins * pirate_a / 100):
        for b in range(int(coins)):
            if b >= (coins * pirate_b / 100):
                for c in range(int(coins)):
                    if c >= (coins * pirate_c / 100) and (a + b + c)==coins:
                        print(f"{a} {b} {c}")
                        flag = True
if flag == False:
    print("EMPTY")
            