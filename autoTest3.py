
import random

n = random.randint(100000, 999999)
left = right = c = 0
print(n)
while n != 0:
    number = n % 10
    if c < 3:
        right += number
    else:
        left += number
    c += 1
    n //= 10
print(left, right)

if left == right:
    print("yes")
else:
    print("no")
