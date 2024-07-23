import json
import os
import logging
from typing import List, Dict


# Настройка логирования
logging.basicConfig(
    filename='log/logfile.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

log = logging.getLogger(__name__)


class Library:
    def __init__(self, filename='data/books.json') -> None:
        self.filename = filename
        self.books: List[Dict] = self.load_books()

    def load_books(self) -> List[Dict]:
        """Загружает книги из JSON-файла.
        Возвращает:
            List[Dict]: Список книг в виде словарей, если файл существует и корректен.
        """
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as file:
                    return json.load(file)
            except (IOError, json.JSONDecodeError) as e:
                log.error(f"Ошибка при загрузке книг:\n{e}")
                return []
        return []

    def save_books(self) -> None:
        """Сохраняет книги в JSON-файл."""
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.books, file, indent=4)
        except IOError as e:
            log.error(f"Ошибка при сохранении книг:\n{e}")

    def get_next_book_id(self) -> str:
        """Определение необходимого id для записи"""
        if not self.books:
            return '1'
        max_id = max(int(book['id']) for book in self.books)
        return str(max_id + 1)

    def add_book(self, title: str, author: str, year: int) -> Dict:
        """Добавляет новую книгу в библиотеку."""
        book_id = self.get_next_book_id()
        new_book: Dict = {
            'id': book_id,
            'title': title,
            'author': author,
            'year': year,
            'status': 'в наличии'
        }
        self.books.append(new_book)
        self.save_books()
        log.info(f"Добавлена книга: {new_book}")
        return new_book

    def delete_book(self, book_id: str) -> bool:
        """Удаляет книгу из библиотеки по её ID."""
        for book in self.books:
            if book['id'] == book_id:
                self.books.remove(book)
                self.save_books()
                log.info(f"Удалена книга с id: {book_id}")
                return True
        raise ValueError("Книга не найдена")

    def find_books_by_title(self, title: str) -> List[Dict]:
        """Поиск книги по названию."""
        return [book for book in self.books if title.lower() in book['title'].lower()]

    def find_books_by_author(self, author: str) -> List[Dict]:
        """Поиск книги по автору."""
        return [book for book in self.books if author.lower() in book['author'].lower()]

    def find_books_by_year(self, year: int) -> List[Dict]:
        """Поиск книги по году."""
        return [book for book in self.books if book['year'] == year]

    def find_books_by_id(self, id: str) -> List[Dict]:
        """Поиск книги по ID."""
        return [book for book in self.books if id in book['id']]

    def display_books(self) -> List[Dict]:
        """Отображение списка всех книг"""
        if not self.books:
            print("\nНет книг для отображения.")
            log.info("Нет книг для отображения.")
            return []
        return self.books

    def update_status(self, book_id: str, new_status: str) -> bool:
        """Обновление статуса книги"""
        if new_status not in ['в наличии', 'выдана']:
            raise ValueError("Неверный статус")
        for book in self.books:
            if book['id'] == book_id:
                book['status'] = new_status
                self.save_books()
                log.info(f"Книга с id {book_id} изменила статус на {new_status}")
                return True
        raise ValueError("Книга не найдена")
