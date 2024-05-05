from book_store import *
from log import Log
from custom_validators import Input_validator
from menus import isbn_error_menu


class Book_manager:
    """
    A class to manage books in the book store.

    Attributes:
        book_store (Book_store): An instance of Book_store to handle book-related operations.
        log (Log): An instance of Log to log book management actions.
        input_validator (Input_validator): An instance of Input_validator to validate user inputs.
    """
    def __init__(self, book_db_path="C:/Users/MOHAK/Desktop/TASK/Redesigning Poor Code/json/book_db.json"):
        """
        Initializes the Book_manager with the given book database path.

        Args:
            book_db_path (str): The file path to the book database JSON file.
        """
        self.book_store=Book_store(book_db_path)
        self.log=Log()
        self.input_validator=Input_validator()

    def is_available(self, book_isbn):
        """
        Checks if a book with the given ISBN is available to be checked_in in the store.

        Args:
            book_isbn (str): The ISBN of the book to check.

        Returns:
            bool: True if the book is available, False otherwise.
        """
        return self.book_store.store_is_available(book_isbn)
    def checkin(self, book_isbn):
        """
        Updates the issue flag of a book to indicate it has been checked in.

        Args:
            book_isbn (str): The ISBN of the book to check in.
        """
        for i in self.book_store.books:
            if i.get_ISBN()==book_isbn:
                i.set_issue_flag(True)
        for i in self.book_store.dict_books:
            if i["book_ISBN"]==book_isbn:
                i["book_issue_flag"]=True
        self.book_store.data["books"]=self.book_store.dict_books
        with open(self.book_store.book_db_path, "w") as file:
            json.dump(self.book_store.data, file, indent=4)


    def checkout(self, book_isbn):
        """
        Updates the issue flag of a book to indicate it has been checked out.

        Args:
            book_isbn (str): The ISBN of the book to check out.
        """
        for i in self.book_store.books:
            if i.get_ISBN()==book_isbn:
                i.set_issue_flag(False)
        for i in self.book_store.dict_books:
            if i["book_ISBN"]==book_isbn:
                i["book_issue_flag"]=False
        self.book_store.data["books"]=self.book_store.dict_books
        with open(self.book_store.book_db_path, "w") as file:
            json.dump(self.book_store.data, file, indent=4)


    def add_book(self):
        """
        Adds a new book to the store.
        
        Returns:
            str: Success or failure message for adding the book.
        """
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
        """
        Retrieves a book from the store based on its ISBN.

        Returns:
            str: The book details if found, or an error message if not found.
        """
        isbn=self.input_validator.empty_string_validator("Enter ISBN to search: ")
        self.log.add_log(f"Book_manager: success, get_book_from_isbn({isbn})")
        response=self.book_store.store_get_book_ISBN(isbn)
        if response=="ISBN not found.":
            return response
        return response.JSONize()
    
    def get_book_from_author(self):
        """
        Retrieves books from the store based on author name.

        Returns:
            str: The list of books with matching author names if found, or an error message if not found.
        """
        author=self.input_validator.empty_string_validator("Enter author to search: ")
        response=self.book_store.store_get_book_author(author)
        if response!="Author not found.":
            self.log.add_log(f"Book_manager: success, get_book_from_author({author})")
            return f"The books with author names that matched with the query are: {response}"
        self.log.add_log(f"Book_manager: failure, get_book_from_author({author})")
        return response
    
    def get_book_from_title(self):
        """
        Retrieves books from the store based on author name.

        Returns:
            str: The list of books with matching author names if found, or an error message if not found.
        """
        title=self.input_validator.empty_string_validator("Enter title to search: ")
        response=self.book_store.store_get_book_title(title)
        if response!="title not found.":
            self.log.add_log(f"Book_manager: success, get_book_from_title({title})")
            return f"The books with title names that matched with the query are: {response}"
        self.log.add_log(f"Book_manager: failure, get_book_from_title({title})")
        return response

    def get_all_books(self):
        """
        Retrieves all books from the store.

        Returns:
            str: The list of all books if found, or a message indicating no books are available.
        """
        response=self.book_store.store_get_all()
        self.log.add_log("Book_manager: success, get_all_books()")
        if response==[]:
            return "No books to display."
        return f"List of all books:{response}"
    
    def delete_book(self):
        """
        Deletes a book from the store.

        Returns:
            str: Success or failure message for deleting the book.
        """
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
        """
        Updates details of a book in the store.

        Returns:
            str: Success or failure message for updating the book details.
        """
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