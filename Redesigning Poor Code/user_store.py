import json
from models import User

class User_store:
    """
    A class representing a user store.

    Attributes:
        - user_db_path (str): The path to the user database file.
        - data (dict): The data read from the user database file.
        - dict_users (list): The list of users in dictionary format.
        - users (list): The list of User objects.
        - existing_ids (set): The set of existing user IDs.
    """
    def __init__(self, user_db_path: str):
        """
        Initializes a User_store object.

        Parameters:
            - user_db_path (str): The path to the user database file.
        """
        self.user_db_path = user_db_path
        with open(self.user_db_path, "r") as file:
            self.data = json.load(file)
            self.dict_users = self.data["users"]
            self.users = [User(user_name=user["user_name"], user_id=user["user_id"]) for user in self.dict_users]
            self.existing_ids = {user.get_id() for user in self.users}

    def check_id(self, user_id):
        """
        Check if a user ID exists.

        Parameters:
            - user_id (str): The user ID to check.

        Returns:
            bool: True if the user ID exists, False otherwise.
        """
        if user_id in self.existing_ids:
            return True
        return False

    def store_add_user(self, new_user: User):
        """
        Add a new user to the store.

        Parameters:
            - new_user (User): The new user to add.
        
        Raises:
            ValueError: If a user with the same ID already exists.
        """
        if self.check_id(new_user.get_id()):
            raise ValueError("A user with the same ID already exists")
        self.users.append(new_user)
        self.dict_users.append({'user_name': new_user.get_name(), 'user_id': new_user.get_id()})
        self.data["users"] = self.dict_users
        self.existing_ids.add(new_user.get_id())
        with open(self.user_db_path, "w") as file:
            json.dump(self.data, file, indent=4)
        return

    def store_get_all(self):
        """
        Get all users from the store.

        Returns:
            list: A list of dictionaries containing user information.
        """
        return [user.JSONize() for user in self.users]

    def store_get_user_id(self, user_id):
        """
        Get a user by ID from the store.

        Parameters:
            - user_id (str): The user ID to search for.

        Returns:
            User or str: The User object if found, otherwise a message indicating user ID not found.
        """
        if not self.check_id(user_id):
            return "User ID not found."
        else:
            for user in self.users:
                if user.get_id() == user_id:
                    return user

    def store_get_user_name(self, user_name):
        """
        Get users by name from the store.

        Parameters:
            - user_name (str): The user name to search for.

        Returns:
            list or str: A list of dictionaries containing user information if found, otherwise a message indicating user name not found.
        """
        ans = []
        for user in self.users:
            if user_name in user.get_name():
                ans.append(user.JSONize())
        if not len(ans):
            return "User name not found."
        return ans

    def store_delete_user(self, user_id):
        """
        Delete a user from the store.

        Parameters:
            - user_id (str): The user ID to delete.

        Returns:
            str: A message indicating the success or failure of deleting the user.
        
        Raises:
            ValueError: If the user ID is not found.
        """
        if not self.check_id(user_id):
            raise ValueError("User ID not found.")
        for id in self.existing_ids:
            if id == user_id:
                user = self.store_get_user_id(user_id)
                self.users.remove(user)
                for i in self.dict_users:
                    if i["user_id"] == user_id:
                        self.dict_users.remove(i)
                        break
                self.data["users"] = self.dict_users
                with open(self.user_db_path, "w") as file:
                    json.dump(self.data, file, indent=4)
                self.existing_ids.remove(id)
                return "User deleted successfully"
        
    def store_update_user(self, user_id, new_name):
        """
        Update a user's name in the store.

        Parameters:
            - user_id (str): The user ID to update.
            - new_name (str): The new name for the user.

        Returns:
            str: A message indicating the success or failure of updating the user name.
        
        Raises:
            ValueError: If the user ID is not found.
        """
        if not self.check_id(user_id):
            raise ValueError("User ID not found.")
        for id in self.existing_ids:
            if id==user_id:
                user=self.store_get_user_id(user_id)
                user.set_name(new_name)
                for i in self.dict_users:
                    if i["user_id"]==user_id:
                        i["user_name"]=new_name
                        break
                self.data["users"]=self.dict_users
                with open(self.user_db_path, "w") as file:
                    json.dump(self.data, file, indent=4)
                return "User updated successfully"
        pass
