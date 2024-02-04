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

def copy_data(file, file2, line):
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    if line > len(lines):
        print('Нет строки с таким номером')
        return
    with open(file2, 'w', encoding='utf-8') as dest:
        dest.write(f'{lines[line -1]}\n')

def main():
    file_name = 'phone_book.txt'
    file_2 = 'phones_copy.txt'
    flag = True
    while flag:
        print('0 - выход')
        print('1 - запись в файл')
        print('2 - показать записи')
        print('3 - найти запись')
        print('4 - скопировать данные')
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
            line_number = int(input('Введите номер строки, которую нужно скопировать в другой файл: '))
            copy_data(file_name, file_2, line_number)


if __name__ == '__main__':
    main()