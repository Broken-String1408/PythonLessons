list1 = [2, 3, 4, 2, 4, 2, 2, 2]
count = 0
for i in set(list1):
    count+= list1.count(i) // 2
print(count)