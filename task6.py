# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233
a = 1
b = 1
n = 21
i = 3
while a + b < n:
    c = b 
    b = a + b
    a = c 
    i += 1
print(i + 1) 


# A = int(input("Введите число"))
# pre, temp = 1, 1
# recent = 2
# i = 4
# while recent <= A:
#     if recent == A:
#         print(f'Номер числа Фибоначчи: {i}')
#         break
#     # temp = pre
#     # pre = recent
#     # recent = recent + temp 
#     pre, recent = recent, pre + recent 
#     i+=1
# else:
#     print(f'Номер числа Фибоначчи: {-1}')