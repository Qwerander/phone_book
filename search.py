from data_actions import display_data

def show_search_menu():
    print("\nМеню поиск:")
    print("1. Поиск по фамилии")
    print("2. Поиск по имени")
    print("3. Поиск по телефону")
    print("0. Вернутся в главное меню")
    return input("Выберите действие: ")


def search_data(phone_book, key, value):
    results = []
    for entry in phone_book:
        if entry[f'{key}'].lower() == value.lower():
            results.append(entry)
    return results

def search_by_value(phone_book):
    while True:
        choice = show_search_menu()
        if choice == '1':
            value = input("Введите фамилию для поиска: ")
            results = search_data(phone_book, 'last_name', value)
            display_data(results, True)
        elif choice == '2':
            value = input("Введите имя для поиска: ")
            results = search_data(phone_book, 'first_name', value)
            display_data(results, True)
        elif choice == '3':
            value = input("Введите телефон для поиска: ")
            results = search_data(phone_book, 'phone_number', value)
            display_data(results, True)
        elif choice == '0':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")
