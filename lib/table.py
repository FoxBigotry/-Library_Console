from typing import List, Dict


def print_books_table(books: List[Dict[str, str]]) -> None:
    """Выводит список книг/книгу в виде таблицы."""
    headers: List[str] = ['ID', 'Title', 'Author', 'Year', 'Status']
    rows: List[List[str]] = [[book['id'], book['title'], book['author'], book['year'], book['status']] for book in books]

    # Поиск максимальной ширины для каждого столбца, для ровного отображения
    column_widths: List[int] = [max(len(str(item)) for item in column) for column in zip(*rows, headers)]

    # Формируется строка для заголовка
    header_row: str = ' | '.join(f"{header:{width}}" for header, width in zip(headers, column_widths))
    separator: str = '-+-'.join('-' * width for width in column_widths)

    # Форматируются строки данных
    data_rows: str = '\n'.join(' | '.join(f"{item:{width}}" for item, width in zip(row, column_widths)) for row in rows)

    print(header_row)
    print(separator)
    print(data_rows)
