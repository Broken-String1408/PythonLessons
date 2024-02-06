# main.py
# FILE_NAME = 'phone_book.txt'
from typing import List
def read_file(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            return lines
    except FileNotFoundError:
        print('файла нет. Сначала введите данные\n')
        return []

def show_data(data: list):
    for line in data:
        print(line)
    # with open('phone_book.txt', 'r', encoding='utf-8') as f:
    #     lines = f.readlines()
    #     for line in lines:
    #         print(line)
    # FileNotFoundError
    # try:
    #     # print('открытие файла')
    #     with open('phone_book.txt', 'r', encoding='utf-8') as f:
    #         lines = f.readlines()
    #         for line in lines:
    #             print(line)
    # except FileNotFoundError as err:
    #     print('файла нет. Сначала введите данные\n')
    # else:
    #     print('else')
    # finally:
    #     print('finally')

def save_data(file):
    print('Введите данные контакта:')
    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    patronymic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    with open(file, 'a', encoding='utf-8') as f:
        f.write(f'{first_name}, {last_name}, {patronymic}, {phone_number}\n')

def search_data(contacts: List[str]):
    # ['Иван, Иванов, Иванович, 123', 'Петр, Иванов, Петрович, 456']
    search_str = input('Введите фамилию для поиска: ')
    founded = []
    # search_idx
    for contact in contacts:
        if search_str.lower() in contact.split(', ')[1].lower():
            founded.append(contact)
    return founded

def delete_data(file_list, founded_data):
    count = 1
    print("выберите данные для удаления")
    for i in founded_data:
        print(count, i)
        count+=1
    k = int(input("Выберите номер элемента для удаления"))
    file_list.pop(file_list.index(founded_data[k - 1]))
    with open("phone_book.txt", "w", encoding="utf-8") as f:
        f.writelines(file_list)
    print("Запись была удалена")

  

def main():
    file_name = 'phone_book.txt'
    flag = True
    while flag:
        print('0 - выход')  
        print('1 - запись в файл')  
        print('2 - показать записи') 
        print('3 - найти запись')
        print('4 - изменить/удалить запись')
        answer = input('Выберите действие: ') 
        if answer == '0':
            flag = False
        elif answer == '1':
            save_data(file_name)
        elif answer == '2':
            data = read_file(file_name)
            show_data(data)
        elif answer == '3':
            data = read_file(file_name)
            founded_data = search_data(data)
            show_data(founded_data)
        elif answer == '4':
            data = read_file(file_name)
            founded_data = search_data(data)
            delete_data(data, founded_data)

if __name__ == '__main__':
    main()