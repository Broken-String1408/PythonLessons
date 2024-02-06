m = [10, 6, 9, 12, 3, 5, 3]

min = m[0] 
max = 0

for apple in m:
    if apple < min:
        min = apple
    elif apple > max:
        max = apple

print(min, max)            