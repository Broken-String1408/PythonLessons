n = 1000
sq = 0
i = 0 
while True:
    sq = 2**i
    if sq > n:
        break
    i += 1
    print(sq)