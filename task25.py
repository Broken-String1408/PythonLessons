string1 = "a a a b c a a d c d d g"
list1 = string1.split(" ")
print(list1)
print()
#list2 = []
dict_count = {}
print(set(list1))
# for x in set(list1):
#     dict_count[x] = 1

for i in range(len(list1)):
    if dict_count.get(list1[i]) is None:
        dict_count[list1[i]] = 0
    else:
        dict_count[list1[i]] += 1
        list1[i] = f"{list1[i]}_{dict_count[list1[i]]}"
    # if list1[i] in list2:
    #     temp = list1[i]
    #     list1[i] = list1[i] + "_" + str(dict_count[list1[i]])
    #     dict_count[temp] +=  1
    #     #dict_count[list1[i]], list1[i] = dict_count[list1[i]] + 1, list1[i] + "_" + str(dict_count[list1[i]])
    # list2.append(list1[i]) 
print(dict_count)

print(*list1)
print(" ".join(list1))