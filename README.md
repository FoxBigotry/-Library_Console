# Система управления библиотекой

Это консольное приложение для управления библиотекой книг. Оно позволяет добавлять, удалять, искать, отображать книги, а также изменять их статус. Приложение хранит данные в формате JSON и предоставляет удобный интерфейс командной строки для взаимодействия с пользователем.

## Функциональность

- **Добавление книги:** Вводите название, автора и год издания книги для добавления её в библиотеку. Каждой книге автоматически присваивается уникальный идентификатор и статус "в наличии".
- **Удаление книги:** Удалите книгу по её уникальному идентификатору.
- **Поиск книги:** Найдите книги по названию, автору или году издания.
- **Отображение всех книг:** Выведите список всех книг с их идентификаторами, названиями, авторами, годами издания и статусами.
- **Изменение статуса книги:** Измените статус книги на "в наличии" или "выдана" по её уникальному идентификатору.

## Технические детали

### Структура проекта

- `app.py` — Основной файл приложения, содержащий логику пользовательского интерфейса.
- `data`
  - `books.json` — Файл для хранения данных о книгах в формате JSON.
- `lib`
  - `choice.py` — Модуль с функциями для обработки пользовательских команд.
  - `library.py` — Модуль, реализующий логику работы с книгами (добавление, удаление, поиск, отображение).
  - `table.py` — Модуль для форматированного вывода книг в виде таблицы.
- `log` 
  - `logfile.log` — Файл логов

### Установка и запуск

1. Клонируйте репозиторий

2. Перейдите в директорию проекта

3. Запустите приложение
```sh
python app.py
```

## Примеры использования

### Добавление книги
```sh
Введите название книги (или 0 для возврата в главное меню):
Гарри Поттер и философский камень
Введите автора (или 0 для возврата в главное меню):
Дж.К. Роулинг
Введите год публикации (или 0 для возврата в главное меню):
1997
```

### Удаление книги
```bash
Введите id книги для удаления  (или 0 для возврата в главное меню)
1
```

### Поиск книги
```sh
Выберите критерий поиска (или 0 для возврата в главное меню):
1. Название
2. Автор
3. Год
Введите свой выбор: 1
Введите название книги (или 0 для возврата в главное меню):
Гарри Поттер
```

### Отображение всех книг
```sh
Книги в библиотеке:
ID   | Title                                   | Author           | Year | Status    
-----+-----------------------------------------+------------------+------+-----------
1    | Гарри Поттер и философский камень       | Дж.К. Роулинг    | 1997 | в наличии 
2    | Гарри Поттер и Тайная комната            | Дж.К. Роулинг    | 1998 | в наличии 

```

### Изменение статуса книги
```sh
Вы знаете id книги для смены статуса?(или 0 для возврата в главное меню):
1. Да
2. Нет
Введите свой выбор: 1
Введите id книги (или 0 для возврата в главное меню):
1
Выберите новый статус (или 0 для возврата в главное меню):
1. в наличии
2. выдана
Введите ваш выбор: 2
```

## Логирование
Все операции с книгами логируются в файл log/logfile.log. Логи содержат информацию о добавлении, удалении книг, а также изменении их статусов.