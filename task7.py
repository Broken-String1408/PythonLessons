days = [5, 25, 123, 23, -20, 30, 40, 50, 10, 10]
res = 0
cur = 0

for day in days:
    if day < 0:
        cur = 0
    else:
        cur += 1    
        res = max(cur, res)

print(res)