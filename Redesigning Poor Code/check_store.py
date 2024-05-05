import json
from models import Check

class Check_store:
    """
    A class to manage check-in and check-out operations for books.
    """
    def __init__(self, check_db_path: str):
        """
        Initializes the Check_store with the given check database path.

        Parameters:
            - check_db_path (str): The file path to the check database.
        """
        self.check_db_path = check_db_path
        with open(self.check_db_path, "r") as file:
            self.data = json.load(file)
            self.dict_checks = self.data["checks"]
            self.checks = [Check(book_isbn=user["book_isbn"], user_id=user["user_id"]) for user in self.dict_checks]

    def check_check(self, check:Check):
        """
        Checks if a given check exists in the check database.

        Parameters:
            - check (Check): The check object to check for.

        Returns:
            - bool: True if the check exists, False otherwise.
        """
        if check.JSONize() in self.dict_checks:
            return True
        return False

    def store_checkin(self, new_check: Check):
        """
        Stores a new check-in record in the check database.

        Parameters:
            - new_check (Check): The check object to be stored.

        Raises:
            - ValueError: If the user has already checked in the book.
        """
        if self.check_check(new_check):
            raise ValueError("This user has already checked in this book")
        self.checks.append(new_check)
        self.dict_checks.append({'user_id': new_check.get_user_id(), 'book_isbn': new_check.get_book_isbn()})
        self.data["checks"] = self.dict_checks
        with open(self.check_db_path, "w") as file:
            json.dump(self.data, file, indent=4)
        return

    def store_get_all(self):
        """
        Retrieves all checks from the check database.

        Returns:
            - list: A list of dictionaries representing all checks.
        """
        return self.dict_checks

    def store_get_check_user_id(self, user_id):
        """
        Retrieves all checks associated with a user ID from the check database.

        Parameters:
            - user_id (str): The ID of the user.

        Returns:
            - list or str: A list of dictionaries representing check information if user found, 
                           otherwise a message indicating no check-ins for the user.
        """
        checks=[]
        for check in self.checks:
            if user_id==check.get_user_id():
                checks.append(check.JSONize())
        if not len(checks):
            return "This user has no checkins"
        return checks
    
    def store_get_check(self, user_id, book_isbn):
        """
        Retrieves a specific check from the check database based on user ID and book ISBN.

        Parameters:
            - user_id (str): The ID of the user.
            - book_isbn (str): The ISBN of the book.

        Returns:
            - Check: The check object if found.

        Raises:
            - ValueError: If the check is not found.
        """
        if self.check_check(Check(user_id, book_isbn)):
            for check in self.checks:
                if check.get_user_id()==user_id and check.get_book_isbn()==book_isbn:
                    return check
        else:
            raise ValueError("Check not found.")


    def store_get_check_book_isbn(self, book_isbn):
        """
        Retrieves all checks associated with a book ISBN from the check database.

        Parameters:
            - book_isbn (str): The ISBN of the book.

        Returns:
            - list or str: A list of dictionaries representing check information if book found, 
                           otherwise a message indicating book hasn't been checked in.
        """
        ans = []
        for check in self.checks:
            if book_isbn in check.get_book_isbn():
                ans.append(check.JSONize())
        if not len(ans):
            return "This book hasn't been checked in."
        return ans

    def store_check_out(self, check:Check):
        """
        Removes a check-out record from the check database.

        Parameters:
            - check (Check): The check object to be removed.

        Raises:
            - ValueError: If the check is not found.
        """
        if not self.check_check(check):
            raise ValueError("Check not found.")
        else:
            obj_check=self.store_get_check(check.get_user_id(), check.get_book_isbn())
            self.checks.remove(obj_check)
            self.dict_checks.remove(obj_check.JSONize())
            self.data["checks"]=self.dict_checks
            with open(self.check_db_path, "w") as file:
                json.dump(self.data, file, indent=4)
