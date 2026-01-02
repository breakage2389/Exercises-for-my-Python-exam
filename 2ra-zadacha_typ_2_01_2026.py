class LibraryBook:
    def __init__(self, isbn, title, author, year, copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.copies = copies

    def borrow(self, count):
        if count <= 0:
            print('Count must be greater than 0.')
            return
        if count > self.copies:
            print('Not enough copies available.')
            return
        self.copies -= count
        print(f'{count} copy(ies) borrowed. Remaining copies: {self.copies}')

    def restock(self, count):
        if count <= 0:
            print('Count must be greater than 0.')
            return
        self.copies += count
        print(f'{count} copy(ies) added. Total copies: {self.copies}')

    def __str__(self):
        return f'ISBN: {self.isbn}, Title: "{self.title}", Author: {self.author}, Year: {self.year}, Copies: {self.copies}'


book_list = []
n = int(input('Number of books: '))
for _ in range(n):
    while True:
        try:
            isbn = int(input('ISBN: '))
            title = input('Title: ')
            author = input('Author: ')
            year = int(input('Year: '))
            copies = int(input('Copies: '))
            book_list.append(LibraryBook(isbn, title, author, year, copies))
            break
        except ValueError:
            print('Wrong input, try again.')
        except KeyboardInterrupt:
            print('Input interrupted.')



def search_by_isbn(book_list, isbn):
    for book in book_list:
        if book.isbn == isbn:
            print(book)
            return
    print('Book not found.')
    print("Available ISBNs:")
    for el in book_list:
        print(el.isbn)


def search_by_author(book_list, author):
    found = [book for book in book_list if book.author == author and book.year > 2000]
    if found:
        for book in found:
            print(book)
    else:
        print(f'No books by {author} after 2000 found.')


def sort_by_year(book_list):
    return sorted(book_list, key=lambda book: book.year, reverse=True)


def remove_unavailable(book_list):
    return [book for book in book_list if book.copies > 0]
