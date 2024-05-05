class Book:
    def __init__(self, book_title="", book_ISBN="", book_author="", book_issue_flag=False):
        self.book_title=book_title
        self.book_ISBN=book_ISBN
        self.book_author=book_author
        self.book_issue_flag=book_issue_flag

    def JSONize(self):
        return {"book_title":self.book_title, "book_ISBN":self.book_ISBN, "book_author":self.book_author, "book_issue_flag":self.book_issue_flag}
    
    def get_ISBN(self):
        return self.book_ISBN
    def set_ISBN(self, new_ISBN):
        self.book_ISBN=new_ISBN

    def get_author(self):
        return self.book_author
    def set_author(self, new_author):
        self.book_author=new_author

    def get_title(self):
        return self.book_title
    def set_title(self, new_title):
        self.book_title=new_title
        
    def get_issue_flag(self):
        return self.book_issue_flag
    def set_issue_flag(self, new_issue_flag):
        self.book_issue_flag=new_issue_flag




class User:
    def __init__(self, user_name="", user_id=""):
        self.user_name=user_name
        self.user_id=user_id

    def JSONize(self):
        return {"user_name":self.user_name, "user_id":self.user_id}
    
    def get_name(self):
        return self.user_name
    def set_name(self, new_name):
        self.user_name=new_name

    def get_id(self):
        return self.user_id
    def set_id(self, new_id):
        self.user_id=new_id



class Check:
    def __init__(self, user_id="", book_isbn=""):
        self.user_id=user_id
        self.book_isbn=book_isbn

    def JSONize(self):
        return {"user_id":self.user_id, "book_isbn":self.book_isbn}
    
    def get_user_id(self):
        return self.user_id
    def set_user_id(self, new_user_id):
        self.user_id=new_user_id

    def get_book_isbn(self):
        return self.book_isbn
    def set_book_isbn(self, new_book_isbn):
        self.book_isbn=new_book_isbn


    