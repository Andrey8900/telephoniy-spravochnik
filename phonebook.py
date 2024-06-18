def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt('phon.txt')

    while choice != 8:
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            last_name = input('Введите фамилию: ')
            results = find_by_lastname(phone_book, last_name)
            if results:
                print("Найденные абоненты:")
                for result in results:
                    print(result)
            else:
                print("Абонент с такой фамилией не найден.")
        elif choice == 3:
            last_name = input('Введите фамилию: ')
            new_number = input('Введите новый номер: ')
            print(change_number(phone_book, last_name, new_number))
            write_txt('phonebook.txt', phone_book)
            print("Изменения сохранены.")
        elif choice == 4:
            last_name = input('Введите фамилию: ')
            print(delete_by_lastname(phone_book, last_name))
            write_txt('phonebook.txt', phone_book)
            print("Изменения сохранены.")
        elif choice == 5:
            number = input('Введите номер телефона: ')
            results = find_by_number(phone_book, number)
            if results:
                print("Найденные абоненты:")
                for result in results:
                    print(result)
            else:
                print("Абонент с таким номером не найден.")
        elif choice == 6:
            user_data = input('Введите новые данные (Фамилия, Имя, Телефон, Описание): ')
            add_user(phone_book, user_data)
            write_txt('phonebook.txt', phone_book)
            print("Новый абонент добавлен и сохранен.")
        elif choice == 7:
            source_file = input('Введите имя исходного файла: ')
            dest_file = input('Введите имя файла назначения: ')
            try:
                line_number = int(input('Введите номер строки для копирования: '))
                copy_line_between_files(source_file, dest_file, line_number)
            except ValueError:
                print("Ошибка: Введите корректное число.")
        
        choice = show_menu()

def show_menu():
    while True:
        try:
            print("\nВыберите необходимое действие:\n"
                  "1. Отобразить весь справочник\n"
                  "2. Найти абонента по фамилии\n"
                  "3. Изменить номер телефона по фамилии\n"
                  "4. Удалить абонента по фамилии\n"
                  "5. Найти абонента по номеру телефона\n"
                  "6. Добавить абонента в справочник\n"
                  "7. Копировать строку из одного файла в другой\n"
                  "8. Закончить работу")
            choice = int(input())
            if 1 <= choice <= 8:
                return choice
            else:
                print("Ошибка: Введите число от 1 до 8.")
        except ValueError:
            print("Ошибка: Введите корректное число.")

def copy_line_between_files(source_file, dest_file, line_number):
    try:
        with open(source_file, 'r', encoding='utf-8') as src:
            lines = src.readlines()
            if line_number <= len(lines):
                line_to_copy = lines[line_number - 1]
                with open(dest_file, 'a', encoding='utf-8') as dst:
                    dst.write(line_to_copy)
                print(f"Строка номер {line_number} успешно скопирована из {source_file} в {dest_file}.")
            else:
                print(f"Ошибка: в файле {source_file} нет строки с номером {line_number}.")
    except FileNotFoundError:
        print(f"Ошибка: файл {source_file} не найден.")

def read_txt(filename):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']

    try:
        with open(filename, 'r', encoding='utf-8') as phb:
            for line in phb:
                record = dict(zip(fields, line.strip().split(',')))
                phone_book.append(record)
    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден.")
    return phone_book

def write_txt(filename, phone_book):
    with open(filename, 'w', encoding='utf-8') as phout:
        for record in phone_book:
            s = ','.join(record.values())
            phout.write(f'{s}\n')

def print_result(phone_book):
    for record in phone_book:
        print(record)

def find_by_lastname(phone_book, last_name):
    return [record for record in phone_book if record['Фамилия'].strip() == last_name]

def change_number(phone_book, last_name, new_number):
    for record in phone_book:
        if record['Фамилия'].strip() == last_name:
            record['Телефон'] = new_number
            return f'Номер телефона для {last_name} изменен на {new_number}'
    return f'Абонент с фамилией {last_name} не найден'

def delete_by_lastname(phone_book, last_name):
    for record in phone_book:
        if record['Фамилия'].strip() == last_name:
            phone_book.remove(record)
            return f'Абонент {last_name} удален'
    return f'Абонент с фамилией {last_name} не найден'

def find_by_number(phone_book, number):
    return [record for record in phone_book if record['Телефон'].strip() == number]

def add_user(phone_book, user_data):
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    user_data_list = user_data.split(',')
    if len(user_data_list) == len(fields):
        record = dict(zip(fields, user_data_list))
        phone_book.append(record)
    else:
        print("Ошибка: Неверный формат данных. Ожидается 'Фамилия, Имя, Телефон, Описание'")

# Запуск программы
if __name__ == "__main__":
    work_with_phonebook()