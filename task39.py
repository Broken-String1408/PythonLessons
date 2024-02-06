from random import randrange
# n = 7
# m = 6
# list1 = [3, 1, 3, 4, 2, 4, 12]
# list2 = [4, 15, 43, 1, 15, 1]

def list_input(number, name = ''):
    return [int(input(f'Введите элемент № {x + 1} для массива {name}: ')) for x in range(number)]

def input_size(name = ''):
    return int(input(f'Введите кол-во элементов массива {name}: '))

def random_list_create(list_size):
    return [randrange(0, 21) for x in range(list_size)]

n = input_size('n')
m = input_size('m')

#list1 = list_input(n, 'n')
#list2 = list_input(m, 'm')

##Заполнение случайными числами##
list1 = random_list_create(n)
list2 = random_list_create(m)

print(list1, '\n',list2, '\n', sep = '')
list3 = [x for x in list1 if x not in list2]
print(list3)