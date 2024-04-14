from data_actions import save_data

def add_record(phone_book: list, file_name):
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    middle_name = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")
    phone_book.append({'last_name': last_name, 'first_name': first_name, 'middle_name': middle_name, 'phone_number': phone_number})
    save_data(file_name, phone_book)

def edit_record(phone_book, file_name):
    print("Для возврата в главное меню введите 0")
    index = int(input("Введите номер записи для редактирования: ")) - 1
    if 0 <= index < len(phone_book):
        entry = phone_book[index]
        print("{:<15} {:<15} {:<15} {:<15}".format("Фамилия", "Имя", "Отчество", "Телефон"))
        print("-" * 70)
        print("{:<15} {:<15} {:<15} {:<15}".format(entry['last_name'], entry['first_name'], entry['middle_name'], entry['phone_number']))
        print("Введите новые данные (оставьте пустым для сохранения старых):")
        last_name = input("Фамилия: ")
        first_name = input("Имя: ")
        middle_name = input("Отчество: ")
        phone_number = input("Телефон: ")

        if not last_name:
            last_name = entry['last_name']
        if not first_name:
            first_name = entry['first_name']
        if not middle_name:
            middle_name = entry['middle_name']
        if not phone_number:
            phone_number = entry['phone_number']

        print("")
        print("Запись с номером {} отредактирована.".format(index + 1))
        phone_book[index] = {'last_name': last_name, 'first_name': first_name, 'middle_name': middle_name, 'phone_number': phone_number}
        save_data(file_name, phone_book)
        print("Новая запись")
        print("{:<15} {:<15} {:<15} {:<15}".format("Фамилия", "Имя", "Отчество", "Телефон"))
        print("-" * 70)
        print("{:<15} {:<15} {:<15} {:<15}".format(last_name, first_name, middle_name, phone_number))
    elif index == -1:
        print("Редактирование отменено.")
    else:
        print("Такой записи нет.")

def delete_record(phone_book, file_name):
    print("Внимание!!! Данное действие не обратимо!")
    print("Для возврата в главное меню введите 0")
    index = int(input("Введите номер записи для удаления: ")) - 1
    if 0 <= index < len(phone_book):
        entry = phone_book[index]
        print("{:<15} {:<15} {:<15} {:<15}".format("Фамилия", "Имя", "Отчество", "Телефон"))
        print("-" * 70)
        print("{:<15} {:<15} {:<15} {:<15}".format(entry['last_name'], entry['first_name'], entry['middle_name'], entry['phone_number']))
        print("Запись {} удалена из справочника.".format(index + 1))
        del phone_book[index]
        save_data(file_name, phone_book)
    elif index == -1:
        print("Удаление отменено.")
    else:
        print("Такой записи нет.")

