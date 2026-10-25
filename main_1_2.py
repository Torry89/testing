# библиотекарь
def get_book(books, book_number):    # передаём каталог книг и номер книги в качестве аргументов функции
    # итерируемся по элементам списка books
    for book in books:
        number = book.get('number') # получаем каждый номер книги по ключу и сравниваем с переданным
        if book_number == number:
            return f"Книга: {book.get('title')}\nАвтор: {book.get('author')}"    # возвращаем требуемые значения по ключу
    return "Книга не найдена в базе"


def get_shelf(directories, book_number):
    """Возвращает номер полки, на которой находится книга"""
    for shelf_number, books_on_shelf in directories.items():
        if book_number in books_on_shelf:
            return shelf_number
    return "Полки с такой книгой не найдено"

def add_book(books, directories, book_number, title, author, shelf_number):
    """
    Добавляет новую книгу в каталог и на полку
    Возвращает сообщение о результате операции
    """
    # Проверяем, существует ли уже книга с таким номером
    for book in books:
        if book['number'] == book_number:
            return "Такая книга уже есть в списке"

        # Создаём новую книгу
    new_book = {
        'number': book_number,
        'title': title,
        'author': author
    }
    books.append(new_book)

    # Добавляем книгу на полку (создаём полку, если её нет)
    if shelf_number not in directories:
        directories.setdefault(shelf_number,[])

    directories[shelf_number].append(book_number)

    return f"Книга добавлена на полку: {shelf_number}"

if __name__ == '__main__':
    books = [
        {'number': 'P-1234', 'title': 'Евгений Онегин', 'author': 'Александр Пушкин'},
        {'number': 'F-88006', 'title': 'Властелин колец', 'author': 'Джон Р. Р. Толкин'},
        {'number': 'D-1122', 'title': 'Безмолвный свидетель', 'author': 'Агата Кристи'}
    ]

    directories = {
        '1': ['P-1234', 'F-88006'],
        '2': ['D-1122'],
        '3': []
    }

    # print(get_book(books, "P-1234"))
    # print(get_shelf(directories, "D-1122"))
    # print(get_book(books, "12345"))
    # print(add_book(books, directories, 'P-1234', 'Евгений Онегин', 'Александр Пушкин', '3'))
    # print(add_book(books, directories, 'N-5678', 'Война и мир', 'Лев Толстой', '3'))
    # print(get_shelf(directories, "N-5678"))
    # print(get_book(books, "N-5678"))
    # print(get_shelf(directories, "12345"))