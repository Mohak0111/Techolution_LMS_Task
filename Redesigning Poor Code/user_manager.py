from user_store import *
from log import Log
from custom_validators import Input_validator
from menus import user_id_error_menu

class User_manager:
    """
    A class representing a user manager.

    Attributes:
        - user_store (User_store): The user store to manage users.
        - log (Log): The log to record user manager activities.
        - input_validator (Input_validator): The input validator for user manager.
    """
    def __init__(self, user_db_path="C:/Users/MOHAK/Desktop/TASK/Redesigning Poor Code/json/user_db.json"):
        """
        Initializes a User_manager object.

        Parameters:
            - user_db_path (str): The path to the user database file.
        """
        self.user_store = User_store(user_db_path)
        self.log = Log()
        self.input_validator = Input_validator()

    def add_user(self):
        """
        Add a new user.

        Returns:
            str: A message indicating the success or failure of adding the user.
        """
        name, user_id = self.input_validator.empty_string_validator("Enter user name: "), self.input_validator.empty_string_validator("Enter user ID: ")
        new_user = User(name, user_id)
        try:
            self.user_store.store_add_user(new_user)
            self.log.add_log(f"User_manager: success, add_user(ID:{new_user.get_id()})")
            return f"User_manager: success, add_user(ID:{new_user.get_id()})"
        except ValueError as e:
            print(f"\n\nERROR: {e}", "Failed to add user.", sep="\n")
            return f"User_manager: failed: add_user(ID:{new_user.get_id()})"

    def get_user_from_id(self):
        """
        Get a user by ID.

        Returns:
            str: A message indicating the success or failure of getting the user.
        """
        user_id = self.input_validator.empty_string_validator("Enter user ID to search: ")
        self.log.add_log(f"User_manager: success, get_user_from_id({user_id})")
        response=self.user_store.store_get_user_id(user_id)
        if response=="User ID not found.":
            return response
        return response.JSONize()

    def get_user_from_name(self):
        """
        Get users by name.

        Returns:
            str: A message indicating the success or failure of getting users by name.
        """
        name = self.input_validator.empty_string_validator("Enter user name to search: ")
        response = self.user_store.store_get_user_name(name)
        if response != "User name not found.":
            self.log.add_log(f"User_manager: success, get_user_from_name({name})")
            return f"The users with names that matched with the query are: {response}"
        self.log.add_log(f"User_manager: failure, get_user_from_name({name})")
        return response

    def get_all_users(self):
        """
        Get all users.

        Returns:
            str: A message containing the list of all users.
        """
        response = self.user_store.store_get_all()
        self.log.add_log("User_manager: success, get_all_users()")
        if response == []:
            return "No users to display."
        return f"List of all users:{response}"

    def delete_user(self):
        """
        Delete a user.

        Returns:
            str: A message indicating the success or failure of deleting the user.
        """
        user_id = self.input_validator.empty_string_validator("Enter user ID: ")
        try:
            self.user_store.store_delete_user(user_id)
            self.log.add_log(f"User_manager: success, delete_user(ID:{user_id})")
            return f"User_manager: success, delete_user(ID:{user_id})"
        except ValueError as e:
            print(f"\n\nERROR: {e}", "Failed to delete user.", sep="\n")
            self.log.add_log(f"User_manager: failure, delete_user(ID:{user_id})")
            return f"User_manager: failure, delete_user(ID:{user_id})"

    def update_user(self):
        """
        Update a user.

        Returns:
            str: A message indicating the success or failure of updating the user.
        """
        user_id = self.input_validator.empty_string_validator("Enter user ID: ")
        choice = 1
        while True:
            try:
                new_name= self.input_validator.empty_string_validator("Enter new name: ")
                self.user_store.store_update_user(user_id, new_name)
                self.log.add_log(f"User_manager: success, update_user(ID:{user_id})")
                return f"User_manager: success, update_user(ID:{user_id})"
            except ValueError as e:
                print(f"\n\nERROR: {e}", "Failed to update user.", sep="\n")
                choice = self.input_validator.choice_validator(1, 2, user_id_error_menu)
                if choice == 1:
                    user_id = self.input_validator.empty_string_validator("Enter user ID: ")
                if choice == 2:
                    break
        self.log.add_log(f"User_manager: failure, update_user(ID:{user_id})")
        return f"User_manager: failure, update_user(ID:{user_id})"
