import os

def read_data(file_name):
    os.system('cls')
    phone_book = []
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                entry = line.strip().split(';')
                phone_book.append({'last_name': entry[0], 'first_name': entry[1], 'middle_name': entry[2], 'phone_number': entry[3]})
        print("Данные успешно импортированы.")
    except FileNotFoundError:
        print("Файл не найден. Создание нового файла.")
        print("Спраочник пустой.")
        with open(file_name, 'w', encoding='utf-8'):
            pass
    return phone_book


def save_data(file_name, phone_book):
    with open(file_name, 'w', encoding='utf-8') as file:
        for entry in phone_book:
            file.write(';'.join([entry['last_name'], entry['first_name'], entry['middle_name'], entry['phone_number']]) + '\n')
    print("Данные успешно сохранены.")


def display_data(phone_book, search=False):
    if phone_book:
        print("{:<5} {:<15} {:<15} {:<15} {:<15}".format("№", "Фамилия", "Имя", "Отчество", "Телефон"))
        print("-" * 70)
        for idx, entry in enumerate(phone_book, start=1):
            print("{:<5} {:<15} {:<15} {:<15} {:<15}".format(idx, entry['last_name'], entry['first_name'], entry['middle_name'], entry['phone_number']))
    elif search:
        print("Записей не найдено.")
    else:
        print("Телефонная книга пуста.")

def export_data(phone_book):
    print("Оставьте пустым для экспорта всего справочника")
    print("Для возврата в главное меню введите 0")
    index = input("Введите номер записи для экспорта: ")
    if index:
        index = int(index) - 1
        if 0 <= index - 1 < len(phone_book):
            entry = phone_book[index]
            file_path = input("Введите имя файла для экспорта (без расширенрия): ") + ".txt"
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write("{},{},{},{}".format(entry['last_name'], entry['first_name'], entry['middle_name'], entry['phone_number']))
            print("Запись успешно экспортирована в файл {}.".format(file_path))
        elif int(index) == -1:
            print("Эксопрт отменен.")
        else:
            print("Нет такой записи.")
    else:
        print("Экспорт всего справочника...")
        file_path = input("Введите имя файла для экспорта (без расширения): ") + ".txt"
        with open(file_path, 'w', encoding='utf-8') as file:
            for entry in phone_book:
                file.write("{},{},{},{}\n".format(entry['last_name'], entry['first_name'], entry['middle_name'], entry['phone_number']))
            print("Справочник успешно экспортирован в файл {}.".format(file_path))



