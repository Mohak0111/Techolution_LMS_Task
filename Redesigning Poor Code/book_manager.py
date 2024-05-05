from book_store import *
from log import Log
from custom_validators import Input_validator
from menus import isbn_error_menu


class Book_manager:
    def __init__(self, book_db_path="C:/Users/MOHAK/Desktop/TASK/Redesigning Poor Code/json/book_db.json"):
        self.book_store=Book_store(book_db_path)
        self.log=Log()
        self.input_validator=Input_validator()


    def add_book(self):
        title, ISBN, author=self.input_validator.empty_string_validator("Enter title: "), self.input_validator.empty_string_validator("Enter ISBN: "), self.input_validator.empty_string_validator("Enter author: ")
        new_book=Book(title, ISBN, author)


        try:
            self.book_store.store_add_book(new_book)
            self.log.add_log(f"Book_manager: success, add_book(ISBN:{new_book.get_ISBN()})")
            return f"Book_manager: success, add_book(ISBN:{new_book.get_ISBN()})"
        

        except ValueError as e:
            print(f"\n\nERROR: {e}", "Failed to add book.", sep="\n")
            choice=self.input_validator.choice_validator(1,2,isbn_error_menu)
            if choice==2:
                self.log.add_log(f"Book_manager: failed: add_book(ISBN:{new_book.get_ISBN()}) duplicate_ISBN")
                return f"Book_manager: failed: add_book(ISBN:{new_book.get_ISBN()}) duplicate_ISBN"
            added_flag=False
            while not added_flag:
                    if choice==2:
                        self.log.add_log(f"Book_manager: failed: add_book(ISBN:{new_book.get_ISBN()}) duplicate_ISBN")
                        return f"Book_manager: failed: add_book(ISBN:{new_book.get_ISBN()}) duplicate_ISBN"
                    new_isbn=self.input_validator.empty_string_validator("enter new isbn: ")
                    try:
                        new_book.set_ISBN(new_isbn)
                        self.book_store.store_add_book(new_book)
                        self.log.add_log(f"Book_manager: success, add_book(ISBN:{new_book.get_ISBN()})")
                        added_flag=True
                        return f"Book_manager: success, add_book(ISBN:{new_book.get_ISBN()})"
                    except ValueError as er:
                        print(f"\n\nERROR: {er}", "Failed to add book.", sep="\n")
                        choice=self.input_validator.choice_validator(1,2,isbn_error_menu)

    def get_book_from_isbn(self):
        isbn=self.input_validator.empty_string_validator("Enter ISBN to search: ")
        self.log.add_log(f"Book_manager: success, get_book_from_isbn({isbn})")
        response=self.book_store.store_get_book_ISBN(isbn)
        if response=="ISBN not found.":
            return response
        return response.JSONize()
    
    def get_book_from_author(self):
        author=self.input_validator.empty_string_validator("Enter author to search: ")
        response=self.book_store.store_get_book_author(author)
        if response!="Author not found.":
            self.log.add_log(f"Book_manager: success, get_book_from_author({author})")
            return f"The books with author names that matched with the query are: {response}"
        self.log.add_log(f"Book_manager: failure, get_book_from_author({author})")
        return response
    
    def get_book_from_title(self):
        title=self.input_validator.empty_string_validator("Enter title to search: ")
        response=self.book_store.store_get_book_title(title)
        if response!="title not found.":
            self.log.add_log(f"Book_manager: success, get_book_from_title({title})")
            return f"The books with title names that matched with the query are: {response}"
        self.log.add_log(f"Book_manager: failure, get_book_from_title({title})")
        return response

    def get_all_books(self):
        response=self.book_store.store_get_all()
        self.log.add_log("Book_manager: success, get_all_books()")
        if response==[]:
            return "No books to display."
        return f"List of all books:{response}"
    
    def delete_book(self):
        isbn=self.input_validator.empty_string_validator("Enter ISBN: ")
        choice=1
        while True:
            try:
                self.book_store.store_delete_book(isbn)
                self.log.add_log(f"Book_manager: success, delete_book(ISBN:{isbn})")
                return f"Book_manager: success, delete_book(ISBN:{isbn})"
            except ValueError as e:
                print(f"\n\nERROR: {e}", "Failed to delete book.", sep="\n")
                choice=self.input_validator.choice_validator(1,2,isbn_error_menu)
                if choice==1:
                    isbn=self.input_validator.empty_string_validator("Enter ISBN: ")
                if choice==2:
                    break
        self.log.add_log(f"Book_manager: failure, delete_book(ISBN:{isbn})")
        return f"Book_manager: failure, delete_book(ISBN:{isbn})"

    def update_book(self):
        isbn=self.input_validator.empty_string_validator("Enter ISBN: ")
        choice=1
        while True:
            try:
                new_title, new_author=self.input_validator.empty_string_validator("Enter new title: "), self.input_validator.empty_string_validator("Enter new author: ")
                self.book_store.store_update_book(isbn, new_title, new_author)
                self.log.add_log(f"Book_manager: success, update_book(ISBN:{isbn})")
                return f"Book_manager: success, update_book(ISBN:{isbn})"
            except ValueError as e:
                print(f"\n\nERROR: {e}", "Failed to update book.", sep="\n")
                choice=self.input_validator.choice_validator(1,2,isbn_error_menu)
                if choice==1:
                    isbn=self.input_validator.empty_string_validator("Enter ISBN: ")
                if choice==2:
                    break
        self.log.add_log(f"Book_manager: failure, update_book(ISBN:{isbn})")
        return f"Book_manager: failure, update_book(ISBN:{isbn})"