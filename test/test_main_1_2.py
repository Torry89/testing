import unittest

from main_1_2 import get_book
from main_1_2 import get_shelf
from main_1_2 import add_book


class TestLibrarian(unittest.TestCase):
    def test_get_book(self):
        books = [
            {'number': 'P-1234', 'title': 'Евгений Онегин', 'author': 'Александр Пушкин'},
            {'number': 'F-88006', 'title': 'Властелин колец', 'author': 'Джон Р. Р. Толкин'},
            {'number': 'D-1122', 'title': 'Безмолвный свидетель', 'author': 'Агата Кристи'}
        ]
        params = (
            ("P-1234",f"Книга: Евгений Онегин\nАвтор: Александр Пушкин"),
            ("12345","Книга не найдена в базе"),
            ("N-5678","Книга не найдена в базе"))
        for i,(book_number,expected) in enumerate(params):
            with self.subTest(i):
                result = get_book(books,book_number)
                self.assertEqual(expected,result)

    def test_get_shelf(self):
        directories = {
            '1': ['P-1234', 'F-88006'],
            '2': ['D-1122'],
            '3': []
        }
        params = (("D-1122","2"),
                  ("N-5678", "Полки с такой книгой не найдено"),
                  ("12345", "Полки с такой книгой не найдено")
        )
        for i,(book_number,expected) in enumerate(params):
            with self.subTest(i):
                result = get_shelf(directories,book_number)
                self.assertEqual(expected,result)

    def test_add_book(self):
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
        params = (('P-1234', 'Евгений Онегин', 'Александр Пушкин', '3','Такая книга уже есть в списке'),
                  ('N-5678', 'Война и мир', 'Лев Толстой', '3','Книга добавлена на полку: 3'))

        for i,(book_number,title,author,shelf_number,expected) in enumerate(params):
            with self.subTest(i):
                result = add_book(books,directories,book_number,title,author,shelf_number)
                self.assertEqual(expected,result)



