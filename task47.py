values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
transormed_values = list(map(lambda x: x + 10, values))
print(values)
print(transormed_values)
print(' '.join(map(str, transormed_values)))