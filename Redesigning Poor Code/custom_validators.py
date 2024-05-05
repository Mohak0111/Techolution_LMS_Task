class Input_validator:
    def choice_validator(self, start, end, menu):
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
        while True:
            s=input(display_string).strip()
            if s.strip()=="":
                print("This input field cannot be empty!")
            else:
                return s