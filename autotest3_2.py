# Требуется найти в массиве list_1 самый близкий по значению элемент 
# к заданному числу k и вывести его.
# Считать, что такой элемент может быть только один. 
# Если значение k совпадает с этим элементом - выведите его.

# Пример:

list_1 = [1, 2, 3, 4, 5, 6, 7]
k = 4
i = 0
n = None
for i in range(len(list_1)):
    if k == list_1[i]:
        n = k
        break
    elif k + 1 == list_1[i]:
        n = k + 1
    elif k - 1 == list_1[i]:
        n = k - 1
    i = i + 1

if n == None:
    print("Error")
else:
    print(n)