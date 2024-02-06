from random import*
def list_input(number, name = ''):
    return [int(input(f'Введите элемент № {x + 1} для массива {name}: ')) for x in range(number)]

def input_size(name = ''):
    return int(input(f'Введите кол-во элементов массива {name}: '))

def random_list_create(list_size):
    return [randrange(0, 21) for x in range(list_size)]


n = input_size()
list1 = random_list_create(n)
print(list1)

count = 0

for x in range(1, n - 1):
    if list1[x] > list1[x - 1] and list1[x] >  list1[x + 1]:
        count += 1
    print(list1[x], count)
print(count)