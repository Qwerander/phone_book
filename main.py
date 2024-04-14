from record_actions import add_record, delete_record, edit_record
from data_actions import display_data, read_data, export_data
from search import search_by_value

def show_main_menu():
    print("\nГлавное меню:")
    print("1. Показать все записи")
    print("2. Добавить запись")
    print("3. Редактировать запись")
    print("4. Удалить запись")
    print("5. Поиск записи")
    print("6. Экспорт данных")
    print("0. Выход")
    return input("Выберите действие: ")


def main():
    file_name = "phone_book.txt"
    phone_book = read_data(file_name)
    while True:
        choice = show_main_menu()
        if choice == '1':
            display_data(phone_book)
        elif choice == '2':
            add_record(phone_book, file_name)
        elif choice == '3':
            edit_record(phone_book, file_name)
        elif choice == '4':
            delete_record(phone_book, file_name)
        elif choice == '5':
            search_by_value(phone_book)
        elif choice == '6':
            export_data(phone_book)
        elif choice == '0':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
