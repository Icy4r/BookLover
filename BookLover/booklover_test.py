import unittest
from booklover import BookLover
import pandas as pd


class BookLoverTestSuite(unittest.TestCase):

    def test_one_add_book(self):
        # setup
        testy = BookLover('testy', 'testy@gmail.com', 'adventure')

        # execute
        testy.add_book('Catcher in the Rye', 4)

        # assert
        self.assertEqual(testy.book_list['book_name'][0], 'Catcher in the Rye')
        self.assertEqual(testy.book_list['book_rating'][0], 4)

    def test_two_add_book(self):
        # setup
        testy = BookLover('testy', 'testy@gmail.com', 'adventure')

        # execute
        testy.add_book('Lord of the Rings: Fellowship of the Ring', 5)
        testy.add_book('Lord of the Rings: Fellowship of the Ring', 4)

        # assert
        self.assertEqual(list(testy.book_list['book_name']).count('Lord of the Rings: Fellowship of the Ring'), 1)

    def test_three_has_read(self):
        # setup
        testy = BookLover('testy', 'testy@gmail.com', 'adventure')
        testy.add_book('To Kill a Mockingbird', 5)

        # execute
        t = testy.has_read('To Kill a Mockingbird')

        # assert
        self.assertTrue(t)

    def test_four_has_read(self):
        # setup
        testy = BookLover('testy', 'testy@gmail.com', 'adventure')
        testy.add_book('To Kill a Mockingbird', 5)

        # execute
        t = testy.has_read('The Book Thief')

        # assert
        self.assertFalse(t)

    def test_five_num_books_read(self):
        # setup
        testy = BookLover('testy', 'testy@gmail.com', 'adventure')
        testy.add_book('To Kill a Mockingbird', 5)
        testy.add_book('The Book Thief', 4)
        testy.add_book('The Great Gatsby', 5)

        # execute
        t = testy.num_books_read()

        # assert
        self.assertEqual(t, 3)

    def test_six_fav_book(self):
        # setup
        testy = BookLover('testy', 'testy@gmail.com', 'adventure')
        testy.add_book('To Kill a Mockingbird', 5)
        testy.add_book('Fahrenheit 451', 2)
        testy.add_book('The Book Thief', 4)
        testy.add_book('The Kite Runner', 3)
        testy.add_book('The Great Gatsby', 5)

        # execute
        favs = testy.fav_books()

        # assert
        self.assertTrue('To Kill a Mockingbird' in list(favs['book_name']))
        self.assertTrue('The Book Thief' in list(favs['book_name']))
        self.assertTrue('The Great Gatsby' in list(favs['book_name']))
        self.assertFalse('Fahrenheit 451' in list(favs['book_name']))
        self.assertFalse('The Kite Runner' in list(favs['book_name']))


if __name__ == '__main__':
    unittest.main(verbosity=3)