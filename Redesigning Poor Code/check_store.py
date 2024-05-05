import json
from models import Check

class Check_store:
    def __init__(self, check_db_path: str):
        self.check_db_path = check_db_path
        with open(self.check_db_path, "r") as file:
            self.data = json.load(file)
            self.dict_checks = self.data["checks"]
            self.checks = [Check(user_name=user["user_name"], user_id=user["user_id"]) for user in self.dict_checks]

    def check_check(self, check:Check):
        if check in self.checks:
            return True
        return False

    def store_checkin(self, new_check: Check):
        if self.check_id(new_check):
            raise ValueError("This user has already checked in this book")
        self.checks.append(new_check)
        self.dict_checks.append({'user_id': new_check.get_user_id(), 'book_isbn': new_check.get_book_isbn()})
        self.data["checks"] = self.dict_checks
        with open(self.check_db_path, "w") as file:
            json.dump(self.data, file, indent=4)
        return

    def store_get_all(self):
        return self.dict_checks

    def store_get_check_user_id(self, user_id):
        checks=[]
        for check in self.checks:
            if user_id==check.get_user_id():
                checks.append(check.JSONize())
        if not len(checks):
            return "This user has no checkins"
        return checks
    
    def store_get_check(self, user_id, book_isbn):
        if self.check_check(Check(user_id, book_isbn)):
            for check in self.checks:
                if check.get_user_id()==user_id and check.get_book_isbn()==book_isbn:
                    return check
        else:
            raise ValueError("Check not found.")


    def store_get_check_book_isbn(self, book_isbn):
        ans = []
        for check in self.checks:
            if book_isbn in check.get_book_isbn():
                ans.append(check.JSONize())
        if not len(ans):
            return "This book hasn't been checked in."
        return ans

    def store_check_out(self, check:Check):
        if not self.check_check(check):
            raise ValueError("Check not found.")
        else:
            obj_check=self.store_get_check(check.get_user_id(), check.get_book_isbn())
            self.checks.remove(obj_check)
            self.dict_checks.remove(obj_check.JSONize())
            self.data["checks"]=self.dict_checks
            with open(self.check_db_path, "w") as file:
                json.dump(self.data, file, indent=4)
