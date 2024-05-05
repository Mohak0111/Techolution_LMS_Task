class Input_validator:
    """
    A class containing methods for input validation.
    """
    def choice_validator(self, start, end, menu):
        """
        Validates the user's choice within a specified range.

        Parameters:
            - start (int): The start of the range.
            - end (int): The end of the range.
            - menu (str): The menu to display.

        Returns:
            - int: The user's choice within the specified range.
        """
        while True:
            print(menu)
            try:
                choice=int(input("Enter choice: "))
                if start<=choice<=end:
                    return choice
                else:
                    print("wrong choice")
            except:
                print("wrong choice")
    def empty_string_validator(self, display_string):
        """
        Validates an input string to ensure it is not empty.

        Parameters:
            - display_string (str): The string to display as a prompt.

        Returns:
            - str: The non-empty input string.
        """
        while True:
            s=input(display_string).strip()
            if s.strip()=="":
                print("This input field cannot be empty!")
            else:
                return s