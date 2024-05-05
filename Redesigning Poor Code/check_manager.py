


from check_store import *
from log import Log
from custom_validators import Input_validator

class Check_manager:
    def __init__(self, check_db_path="C:/Users/MOHAK/Desktop/TASK/Redesigning Poor Code/json/check_db.json"):
        self.check_store = Check_store(check_db_path)
        self.log = Log()
        self.input_validator = Input_validator()

    def check_in(self, user_id, isbn):
        new_check = Check(user_id=user_id, book_isbn=isbn)
        try:
            self.check_store.store_checkin(new_check)
            self.log.add_log(f"Check_manager: success, checkin(ID:{new_check.get_user_id()}, ISBN:{new_check.get_book_isbn()})")
            return f"Check_manager: success, checkin(ID:{new_check.get_user_id()}, ISBN:{new_check.get_book_isbn()})"
        except ValueError as e:
            print(f"\n\nERROR: {e}", "Failed to checkin.", sep="\n")
            return f"Check_manager: failed: checkin(ID:{new_check.get_user_id()}, ISBN:{new_check.get_book_isbn()})"

    def get_check_from_user_id(self, user_id):
        self.log.add_log(f"Check_manager: success, get_check_from_user_id({user_id})")
        response=self.check_store.store_get_check_user_id(user_id)
        if response=="This user has no checkins":
            return response
        return [i.JSONize() for i in response]

    def get_check_from_book_isbn(self, isbn):
        self.log.add_log(f"Check_manager: success, get_user_from_name({isbn})")
        response = self.check_store.store_get_check_book_isbn(isbn)
        if response=="This book hasn't been checked in.":
            return response
        return [i.JSONize() for i in response]

    def get_all_checks(self):
        response = self.check_store.store_get_all()
        self.log.add_log("Check_manager: success, get_all_checks()")
        if response == []:
            return "No chccks to display."
        return f"List of all checks:{response}"

    def check_out(self, user_id, book_isbn):
        try:
            check=self.check_store.store_get_check(user_id, book_isbn)
            self.check_store.store_check_out(check)
            self.log.add_log(f"Check_manager: success, check_out({check.get_user_id, check.get_book_isbn})")
            return f"Check_manager: success, check_out({check.get_user_id, check.get_book_isbn})"
        except ValueError as e:
            self.log.add_log(f"Check_manager: success, check_out({user_id, book_isbn})")
            return f"Failure, {e}"