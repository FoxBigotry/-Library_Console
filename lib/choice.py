from lib.library import Library
from lib.table import print_books_table
from typing import Optional, List, Dict
from datetime import datetime

library = Library()


def unknown_id() -> bool:
    """
    Обрабатывает случай, когда пользователь не знает ID книги.
    Предлагает пользователю варианты:
    1. Найти книгу по критериям.
    2. Показать все книги.

    Возвращает:
        bool: True, если пользователь решил вернуться в главное меню.
    """
    while True:
        choice: str = input("\nХорошо, давайте узнаем id нужной вам книги (или 0 для возврата в главное меню):\n"
                            "1. Найти книгу.\n"
                            "2. Показать все книги\n"
                            "Введите свой выбор: ")
        if choice == '1':
            if choice_search():
                return True
            return False
        elif choice == '2':
            choice_display()
            return False
        elif choice == '0':
            return True
        else:
            print("\nНекорректный выбор. Пожалуйста, повторите.")


def choice_add() -> None:
    """
    Обрабатывает добавление новой книги в библиотеку.
    Пользователь может вернуться в главное меню, введя 0.
    """
    title: str = input("\nВведите название книги (или 0 для возврата в главное меню):\n")
    if title == '0':
        return
    author: str = input("Введите автора (или 0 для возврата в главное меню):\n")
    if author == '0':
        return

    year: Optional[int] = None
    while year is None:
        year_input: str = input("Введите год публикации (или 0 для возврата в главное меню):\n")
        if year_input == '0':
            return
        try:
            year: int = int(year_input)
            if year > datetime.now().year:
                print(f"Ошибка: Год публикации не может быть больше текущего года ({datetime.now().year}).")
                year = None
            elif year < 0:
                print("Ошибка: Год публикации не может быть отрицательным.")
                year = None
        except ValueError:
            print("Ошибка: Год публикации должен быть числом.")

    book: Dict = library.add_book(title, author, year)
    print(f"\nДобавлена книга:")
    print_books_table([book])


def delete_try() -> bool:
    """
    Запрашивает ID книги для удаления и пытается удалить её.

    Возвращает:
        bool: True, если пользователь решил вернуться в главное меню.
    """
    while True:
        book_id: str = input("Введите id книги для удаления  (или 0 для возврата в главное меню)\n")
        if book_id == '0':
            return True
        book_for_table: List[Dict] = library.find_books_by_id(book_id)
        if not book_for_table:
            print(f"\nПростите, данный id  не найден.\n"
                  f"Удаление не произведено.")
            return True
        try:
            if library.delete_book(book_id):
                print(f"\nБыла удалена книга:")
                print_books_table(book_for_table)
            return True
        except ValueError as e:
            print(f"\nУдаление не произведено. Причина:\n{e}")
            return True


def choice_delete() -> None:
    """
    Обрабатывает удаление книги по её ID. Позволяет вернуться в главное меню,
    введя 0. Запрашивает ID книги и удаляет её, если ID найден.
    """
    while True:
        choice_del: str = input("\nВы знаете id книги для удаления? (или 0 для возврата в главное меню)\n"
                                "1. Да\n"
                                "2. Нет\n"
                                "Введите свой выбор: ")
        if choice_del == '0':
            return
        elif choice_del == '2':
            if unknown_id():
                return
            else:
                if delete_try():
                    return
        elif choice_del == '1':
            if delete_try():
                return
        else:
            print("\nНекорректный выбор. Пожалуйста, повторите.")


def choice_search() -> bool:
    """
    Поиск книги в библиотеке по выбранному критерию.
    Позволяет вернуться в главное меню, введя 0.

    Возвращает:
        bool: True, если пользователь решил вернуться в главное меню.
    """
    while True:
        search: str = input("\nВыберите критерий поиска (или 0 для возврата в главное меню):"
                            "\n1. Название"
                            "\n2. Автор"
                            "\n3. Год"
                            "\nВведите свой выбор: ")
        if search == '0':
            return True
        elif search == '1':
            title: str = input("Введите название книги (или 0 для возврата в главное меню):\n")
            if title == '0':
                return True
            books: List[Dict] = library.find_books_by_title(title)
            break
        elif search == '2':
            author: str = input("Введите автора книги (или 0 для возврата в главное меню):\n")
            if author == '0':
                return True
            books: List[Dict] = library.find_books_by_author(author)
            break
        elif search == '3':
            try:
                year = int(input("Введите год публикации (или 0 для возврата в главное меню):\n"))
                if year == 0:
                    return True
                books: List[Dict] = library.find_books_by_year(year)
                break
            except ValueError:
                print("Некорректный ввод. Пожалуйста, введите числовое значение для года.")
        else:
            print("\nНекорректный выбор. Пожалуйста, повторите.")

    if books:
        print("\nНайденые книги:")
        print_books_table(books)
    else:
        print("\nКниги не найдены.")
        return True


def choice_display() -> None:
    """
    Отображает все книги в библиотеке.
    Выводит сообщение, если книг нет.
    """
    books: List[Dict] = library.display_books()
    if books:
        print("\nКниги в библиотеке:")
        print_books_table(books)


def choice_change_status() -> None:
    """
    Обрабатывает изменение статуса книги по её ID. Позволяет вернуться в главное меню,
    введя 0. Запрашивает ID книги и новый статус, если ID найден.
    """
    while True:
        choice_status: str = input("\nВы знаете id книги для смены статуса?(или 0 для возврата в главное меню):\n"
                                   "1. Да\n"
                                   "2. Нет\n"
                                   "Введите свой выбор: ")
        if choice_status == '0':
            return
        elif choice_status == '1':
            break
        elif choice_status == '2':
            if unknown_id():
                return
            else:
                break
        else:
            print("Некорректный выбор. Пожалуйста, повторите.")

    while True:
        book_id: str = input("Введите id книги (или 0 для возврата в главное меню):\n")
        if book_id == '0':
            return
        book_for_table: List[Dict] = library.find_books_by_id(book_id)
        if not book_for_table:
            print(f"\nПростите, данный id {book_id} не найден. Попробуйте снова.")
        else:
            break

    while True:
        status_choice: str = input("Выберите новый статус (или 0 для возврата в главное меню):\n"
                                   "1. в наличии\n"
                                   "2. выдана\n"
                                   "Введите ваш выбор: ")
        if status_choice == '0':
            return
        elif status_choice in {'1', '2'}:
            status = {1: 'в наличии', 2: 'выдана'}[int(status_choice)]
            break
        else:
            print("Некорректный выбор. Пожалуйста, повторите.")

    if library.update_status(book_id, status):
        print(f"\nКнига с id {book_id} изменила статус на {status}")
        print_books_table(book_for_table)
    else:
        print("\nНе удалось обновить статус книги. Пожалуйста, попробуйте снова.")
