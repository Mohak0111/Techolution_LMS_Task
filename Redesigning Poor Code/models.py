class Book:
    """
    A class representing a book.

    Attributes:
        - book_title (str): The title of the book.
        - book_ISBN (str): The ISBN of the book.
        - book_author (str): The author of the book.
        - book_issue_flag (bool): Flag indicating if the book is issued or not.
    """
    def __init__(self, book_title="", book_ISBN="", book_author="", book_issue_flag=False):
        """
        Initializes a Book object.

        Parameters:
            - book_title (str): The title of the book.
            - book_ISBN (str): The ISBN of the book.
            - book_author (str): The author of the book.
            - book_issue_flag (bool): Flag indicating if the book is issued or not.
        """
        self.book_title=book_title
        self.book_ISBN=book_ISBN
        self.book_author=book_author
        self.book_issue_flag=book_issue_flag

    def JSONize(self):
        """
        Returns a JSON representation of the book.

        Returns:
            dict: A dictionary containing the book information.
        """
        return {"book_title":self.book_title, "book_ISBN":self.book_ISBN, "book_author":self.book_author, "book_issue_flag":self.book_issue_flag}
    
    def get_ISBN(self):
        """
        Get the ISBN of the book.

        Returns:
            str: The ISBN of the book.
        """
        return self.book_ISBN
    def set_ISBN(self, new_ISBN):
        """
        Set the ISBN of the book.

        Parameters:
            new_ISBN (str): The new ISBN to be set.
        """
        self.book_ISBN=new_ISBN

    def get_author(self):
        """
        Get the author of the book.

        Returns:
            str: The author of the book.
        """
        return self.book_author
    def set_author(self, new_author):
        """
        Set the author of the book.

        Parameters:
            new_author (str): The new author to be set.
        """
        self.book_author=new_author

    def get_title(self):
        """
        Get the title of the book.

        Returns:
            str: The title of the book.
        """
        return self.book_title
    def set_title(self, new_title):
        """
        Set the title of the book.

        Parameters:
            new_title (str): The new title to be set.
        """
        self.book_title=new_title
        
    def get_issue_flag(self):
        """
        Get the issue flag of the book.

        Returns:
            bool: The issue flag of the book.
        """
        return self.book_issue_flag
    def set_issue_flag(self, new_issue_flag):
        """
        Set the issue flag of the book.

        Parameters:
            new_issue_flag (bool): The new issue flag to be set.
        """
        self.book_issue_flag=new_issue_flag




class User:
    """
    A class representing a user.

    Attributes:
        - user_name (str): The name of the user.
        - user_id (str): The ID of the user.
    """
    def __init__(self, user_name="", user_id=""):
        """
        Initializes a User object.

        Parameters:
            - user_name (str): The name of the user.
            - user_id (str): The ID of the user.
        """
        self.user_name=user_name
        self.user_id=user_id

    def JSONize(self):
        """
        Returns a JSON representation of the user.

        Returns:
            dict: A dictionary containing the user information.
        """
        return {"user_name":self.user_name, "user_id":self.user_id}
    
    def get_name(self):
        """
        Get the name of the user.

        Returns:
            str: The name of the user.
        """
        return self.user_name
    def set_name(self, new_name):
        """
        Set the name of the user.

        Parameters:
            new_name (str): The new name to be set.
        """
        self.user_name=new_name

    def get_id(self):
        """
        Get the ID of the user.

        Returns:
            str: The ID of the user.
        """
        return self.user_id
    def set_id(self, new_id):
        """
        Set the ID of the user.

        Parameters:
            new_id (str): The new ID to be set.
        """
        self.user_id=new_id



class Check:
    """
    A class representing a check.

    Attributes:
        - user_id (str): The ID of the user.
        - book_isbn (str): The ISBN of the book.
    """
    def __init__(self, user_id="", book_isbn=""):
        """
        Initializes a Check object.

        Parameters:
            - user_id (str): The ID of the user.
            - book_isbn (str): The ISBN of the book.
        """
        self.user_id=user_id
        self.book_isbn=book_isbn

    def JSONize(self):
        """
        Returns a JSON representation of the check.

        Returns:
            dict: A dictionary containing the check information.
        """
        return {"user_id":self.user_id, "book_isbn":self.book_isbn}
    
    def get_user_id(self):
        """
        Get the ID of the user.

        Returns:
            str: The ID of the user.
        """
        return self.user_id
    def set_user_id(self, new_user_id):
        """
        Set the ID of the user.

        Parameters:
            new_user_id (str): The new ID to be set.
        """
        self.user_id=new_user_id

    def get_book_isbn(self):
        """
        Get the ISBN of the book.

        Returns:
            str: The ISBN of the book.
        """
        return self.book_isbn
    def set_book_isbn(self, new_book_isbn):
        """
        Set the ISBN of the book.

        Parameters:
            new_book_isbn (str): The new ISBN to be set.
        """
        self.book_isbn=new_book_isbn


    