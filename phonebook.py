def read_file(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            return lines
    except FileNotFoundError as err:
       print('файла нет', 'error:', err)
       return []


def show_data(data: list):
    for line in data:
        print(line)


def save_data(file):
    print('Введите данные контакта')
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    with open(file, 'a', encoding='utf-8') as f:
        f.write(f'{last_name}, {first_name}, {patronymic}, {phone_number}\n')


def search_data(contacts: list[str]): # Функция поиска данных
    founded = []
    print('0 - поиск по фамилии')
    print('1 - поиск по имени')
    print('2 - поиск по отчеству')
    print('3 - поиск по номеру телефона')
    search_idx = input('Выберите вариант поиска: ') # для поиска по фамилии, имени, отчеству или номеру телефона
    #search_idx для поиска по фамилии, имени, отчеству
    search_str = input('Введите данные для поиска: ')
    for contact in contacts:
        if search_str.lower() in contact.split(', ')[int(search_idx)].lower(): # разделитель - запятая, поиск по первому индексу (по фамилии)
            founded.append(contact)
    return founded

# def copy_data(file, file2, line):
#     with open(file, 'r', encoding='utf-8') as f:
#         lines = f.readlines()
#     if line > len(lines):
#         print('Нет строки с таким номером')
#         return
#     with open(file2, 'w', encoding='utf-8') as dest:
#         dest.write(f'{lines[line -1]}\n')
#         for i in range(len(lines)):
#             if i != line-1:
#                 dest.write(lines[i])
def new_save(file, data):
    if len(data)>0:
        with open(file, 'w', encoding='utf-8') as f:
            f.seek(0)
            f.writelines(data)
        return True


def edit_data (data, chng_index, file):
    print('0 - Фамилию')
    print('1 - Имя')
    print('2 - Отчество')
    print('3 - Телефон')
    choice = int(input(('Выберите, что хотите изменить: ')))
    temp = data[chng_index].split(', ')
    temp[choice] = input('Введите новое значение: ')
    data[chng_index] = ', '.join(temp)+'\n'
    new_save(file, data)

def delete_data(data, idx, file): 
    del data[idx]
    new_save(file, data)

def copy_to_file(data, idx, file_2):
    if idx > len(data):
        print('Нет строки с таким номером')
        return
    with open(file_2, 'a', encoding='utf-8') as export:
        export.write(f'{data[idx]}\n')


def main():
    file_name = 'phone_book.txt'
    file_name_copy = 'phone_book_copy.txt'
    flag = True
    while flag:
        print('0 - выход')
        print('1 - запись в файл')
        print('2 - показать записи')
        print('3 - найти запись')
        print('4 - изменить данные')
        print('5 - удалить данные из справочника')
        print('6 - копировать данные о пользователе в другой файл')
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
            show_data(data) 
            change_index = int(input('Чтобы отредактировать данные - введите номер строки:'))-1
            edit_data(data, change_index, file_name)
        elif answer == '5':
            data = read_file(file_name) 
            idx_delete = int(input('Введите строку, которую надо удалить: ')) - 1
            delete_data(data, idx_delete, file_name)
        elif answer == '6':
            data = read_file(file_name) 
            idx_copy = int(input('Введите номер строки, для экспорта: ')) - 1
            copy_to_file(data, idx_copy, file_name_copy)

if __name__ == '__main__':
    main()