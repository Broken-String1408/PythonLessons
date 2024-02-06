# def f (x):
#     return x*x


# a = f

# print((a(5)))
# print((f(5)))



# def calk2(a, b):
#     return a*b

# def math(op, x, y):
#     print(op(x, y))


# math(lambda a,b: a + b, 5, 45) 

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()

# for i in data:
#     if i % 2 == 0:
#         res.append((i, i**2))

# print(res)




data = [1, 2, 3, 5, 8, 15, 23, 38]
res = map(int, data)
res = filter(lambda x: x % 2 == 0, res)
res = list(map(lambda x: (x, x**2), res))
print(res)