import lib.choice as pick


def main():
    """
    Основная функция, управляющая меню системы управления библиотекой.
    """
    while True:
        choice: str = input("\nДобро пожаловать в систему управления библиотекой\n"
                            "1. Добавить книгу\n"
                            "2. Удалить книгу\n"
                            "3. Найти книгу\n"
                            "4. Показать все книги\n"
                            "5. Обновить статус книги\n"
                            "6. Выход\n"
                            "Введите свой выбор: ")

        if choice == '1':
            pick.choice_add()

        elif choice == '2':
            pick.choice_delete()

        elif choice == '3':
            pick.choice_search()

        elif choice == '4':
            pick.choice_display()

        elif choice == '5':
            pick.choice_change_status()

        elif choice == '6':
            break

        else:
            print("Неизвестная команда, пожалуйста, сделайте выбор снова.")


if __name__ == "__main__":
    main()
