def same_by(characteristic, objects):
    list1 = list(map(characteristic, objects))
    list2 = list(filter(lambda x: x ==False, list1))
    if len(list2) == 0: 
        print('same')
    else: 
        print('not the same')

def same_by2(characteristic, objects):
    if len(objects) == 0: return True
    temp = characteristic(objects[0])
    list1 = list(map(lambda x: characteristic(x) == temp, objects))
    # print(list1)
    # print(all(list1))
    # print(any(list1))
    return all(list1)


values = [0, 2, 10, 8, '4']
values2 = ['жираф', 'слон', 234]
values3 = ()

sample1 = lambda x: x % 2 == 0 # Четность
sample2 = lambda x: x >= 0     # Неотрицательное число
sample3 = lambda x: isinstance(x, str) # Строковый тип
sample4 = lambda x: isinstance(x, int) # Целочисленный тип
sample5 = lambda x: x is None #Пустое множество


print(same_by2(sample3, values2))