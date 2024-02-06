# def delt(n):
#     dl = set()
#     for i in range(2,int(n**0.5)+1):
#         if n % i == 0:
#             dl.add(i)
#             dl.add(n//i)
#     return sum(dl)
# k = int(input('Введите число к '))
# c = set()
# for i in range(k):
#     for j in range(i+1,k):
#         if delt(i)+1 == j and delt(j)+1 == i:
#             c.add((i,j))
# print(c)


def sum_div(n: int):
    sum_ = 1
    # range(2, 111) = 2, 3, 4, ... 109, 110
    # 221 // 2 +1 = 110 + 1
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            sum_ += i
    return sum_

# 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 и 110
# print(sum_div(220))  # => 284
# 1, 2, 4, 71 и 142
# print(sum_div(284))  # => 220

def friendly_nums(k: int):
    res = []
    for i in range(2, k):
        j = sum_div(i)
        if sum_div(j) == i and i < j < k:
            res.append((i, j))
        # for j in range(2, k):
        #     if sum_div(i) == j and sum_div(j) == i and i < j:
        #         res.append((i, j))
    return res


print(friendly_nums(13000))