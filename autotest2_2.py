s = 1443999
p = 518209185420

x = 1 
while True:
    if p % x == 0:
        y = p // x
        if y < x:
            break
        if y * x == p and y + x == s:
            print(x, y)
    x += 1

