# Ian Yung (icy4r)
# 7.28.2023
# booklover.py

# import statement
import pandas as pd

class BookLover():
    '''
    Creates a book lover person and all their info.
    '''

    def __init__(self, name, email, favgenre, num_books=0, book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name = name
        self.email = email
        self.favgenre = favgenre
        self.num_books = num_books
        self.book_list = book_list

    # methods
    def add_book(self, book_name, rating):

        if self.has_read(book_name):
            print(f"{book_name} is already in {self.name}'s book list!")
            return

        else:
            new_book = pd.DataFrame({
                'book_name': book_name,
                'book_rating': rating
            }, index = [0])
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            self.num_books = len(self.book_list)

    def has_read(self, book_name):
        if book_name in list(self.book_list['book_name']):
            return True
        return False

    def num_books_read(self):
        return len(self.book_list)

    def fav_books(self):
        return self.book_list[self.book_list['book_rating'] > 3]
