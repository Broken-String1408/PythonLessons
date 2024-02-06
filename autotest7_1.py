# def print_operation_table(operation, num_rows, num_columns):
#     if num_rows < 2:
#         print("ОШИБКА! Размерности таблицы должны быть больше 2!")
#         return
#     res = [[operation(row, col) for row in range(1, num_columns + 1)] for col in range(1, num_rows + 1)]

#     for i in res:
#         print(*[f"{x} " for x in i])


def print_operation_table(operation, num_rows = 9, num_columns = 9):
    if num_rows < 2:
        print("ОШИБКА! Размерности таблицы должны быть больше 2!")
        return
    for i in range(1, num_rows + 1):
        answer = []
        for j in range(1, num_columns + 1):
                answer.append(str(operation(i, j)))
        print(' '.join(answer))

print_operation_table(lambda x, y: x * y)