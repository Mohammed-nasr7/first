class Book:
   

    def __init__(self, title, author):
      
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
      
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
       
        self._is_checked_out = False

    def is_available(self):
        
        return not self._is_checked_out


class Library:
   

    def __init__(self):
        self._books = []  # Private list to store books

    def add_book(self, book):
       
        self._books.append(book)

    def check_out_book(self, title):
        
        for book in self._books:
            if book.title == title:
                if book.check_out():
                    return True
                else:
                    print(f"'{title}' is already checked out.")
                    return False
        print(f"'{title}' not found in the library.")
        return False

    def return_book(self, title):
        
        for book in self._books:
            if book.title == title:
                book.return_book()
                return True
        print(f"'{title}' not found in the library.")
        return False

    def list_available_books(self):
       
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No available books.")