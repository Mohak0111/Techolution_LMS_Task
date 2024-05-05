import json
from models import Book



class Book_store:
    """
    A class to manage books in the book store.
    """
    def __init__(self, book_db_path:str):
        """
        Initializes the Book_store with the given book database path.

        Parameters:
            - book_db_path (str): The file path to the book database.
        """
        self.book_db_path=book_db_path
        with open(self.book_db_path, "r") as file:
            self.data=json.load(file)
            self.dict_books=self.data["books"]
            self.books=[Book(book_title=book["book_title"],book_ISBN=book["book_ISBN"],book_author=book["book_author"], book_issue_flag=book["book_issue_flag"]) for book in self.dict_books]
            self.existing_ISBNs={book.get_ISBN() for book in self.books}
    
    def check_ISBN(self, ISBN):
        """
        Checks if a book with the given ISBN exists in the store.

        Parameters:
            - ISBN (str): The ISBN of the book to check.

        Returns:
            - bool: True if the book exists, False otherwise.
        """
        if ISBN in self.existing_ISBNs:
            return True
        return False
            
        
    def store_add_book(self, new_book:Book):
        """
        Adds a new book to the store.

        Parameters:
            - new_book (Book): The book object to add.

        Raises:
            - ValueError: If a book with the same ISBN already exists.
        """
        if self.check_ISBN(new_book.get_ISBN()):
            raise ValueError("A book with the same ISBN already exists")
        self.books.append(new_book)
        self.dict_books.append({'book_title':new_book.get_title(),'book_ISBN':new_book.get_ISBN(), 'book_author':new_book.get_author(), 'book_issue_flag':False})
        self.data["books"]=self.dict_books
        self.existing_ISBNs.add(new_book.get_ISBN())
        with open(self.book_db_path,"w") as file:
            json.dump(self.data, file, indent=4)
        return
    
    
    def store_get_all(self):
        """
        Retrieves all books from the store.

        Returns:
            - list: A list of dictionaries representing book information.
        """
        return [book.JSONize() for book in self.books]
    
    def store_is_available(self, isbn):
        """
        Checks if a book with the given ISBN is available in the store.

        Parameters:
            - isbn (str): The ISBN of the book to check availability.

        Returns:
            - bool: True if the book is available, False otherwise.
        """
        for book in self.books:
            if book.get_ISBN()==isbn:
                return book.get_issue_flag()
    
    def store_get_book_ISBN(self, ISBN):
        """
        Retrieves a book from the store based on ISBN.

        Parameters:
            - ISBN (str): The ISBN of the book to retrieve.

        Returns:
            - Book or str: The book object if found, otherwise a message indicating ISBN not found.
        """
        if not self.check_ISBN(ISBN):
            return "ISBN not found."
        else:
            for book in self.books:
                if book.get_ISBN()==ISBN:
                    return book
                
                
    def store_get_book_author(self, author):
        """
        Retrieves books from the store based on author.

        Parameters:
            - author (str): The author's name to search for.

        Returns:
            - list or str: A list of dictionaries representing book information if author found, 
                           otherwise a message indicating author not found.
        """
        ans=[]
        for book in self.books:
            if author in book.get_author():
                ans.append(book.JSONize())
        if not len(ans):
            return "Author not found."
        return ans

    def store_get_book_title(self, title):
        """
        Retrieves books from the store based on title.

        Parameters:
            - title (str): The title to search for.

        Returns:
            - list or str: A list of dictionaries representing book information if title found, 
                           otherwise a message indicating title not found.
        """
        ans=[]
        for book in self.books:
            if title in book.get_title():
                ans.append(book.JSONize())
        if not len(ans):
            return "title not found."
        return ans
    
    def store_delete_book(self, ISBN):
        """
        Deletes a book from the store based on ISBN.

        Parameters:
            - ISBN (str): The ISBN of the book to delete.

        Returns:
            - str: A message indicating the success or failure of the deletion operation.
        """
        if not self.check_ISBN(ISBN):
            raise ValueError("ISBN not found.")
        for isbn in self.existing_ISBNs:
            if isbn==ISBN:
                book=self.store_get_book_ISBN(ISBN)
                self.books.remove(book)
                for i in self.dict_books:
                    if i["book_ISBN"]==ISBN:
                        self.dict_books.remove(i)
                        break
                self.data["books"]=self.dict_books
                with open(self.book_db_path, "w") as file:
                    json.dump(self.data, file, indent=4)
                self.existing_ISBNs.remove(isbn)
                return "Book deleted successfully"
        pass
    
    def store_update_book(self, ISBN, new_title, new_author):
        """
        Updates the title and author of a book in the store based on ISBN.

        Parameters:
            - ISBN (str): The ISBN of the book to update.
            - new_title (str): The new title for the book.
            - new_author (str): The new author for the book.

        Returns:
            - str: A message indicating the success or failure of the update operation.
        """
        if not self.check_ISBN(ISBN):
            raise ValueError("ISBN not found.")
        for isbn in self.existing_ISBNs:
            if isbn==ISBN:
                book=self.store_get_book_ISBN(ISBN)
                book.set_author(new_author)
                book.set_title(new_title)
                for i in self.dict_books:
                    if i["book_ISBN"]==ISBN:
                        i["book_title"], i["book_author"]=new_title, new_author
                        break
                self.data["books"]=self.dict_books
                with open(self.book_db_path, "w") as file:
                    json.dump(self.data, file, indent=4)
                return "Book updated successfully"
        pass
