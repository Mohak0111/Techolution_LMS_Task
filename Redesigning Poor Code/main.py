from book_manager import Book_manager
from user_manager import User_manager
from check_manager import Check_manager
from menus import main_menu, manage_books, manage_users, check_menu
from custom_validators import Input_validator




def main():
    book_manager=Book_manager()
    user_manager=User_manager()
    check_manager=Check_manager()
    input_validator=Input_validator()
    while True:
        choice = input_validator.choice_validator(1, 4, main_menu)
        if choice==1:# manage books
            while True:
                book_choice=input_validator.choice_validator(1, 8, manage_books)
                if book_choice== 1:
                    print(book_manager.add_book())
                elif book_choice== 2:
                    print(book_manager.get_book_from_title())
                elif book_choice== 3:
                    print(book_manager.get_book_from_author())
                elif book_choice== 4:
                    print(book_manager.get_book_from_isbn())
                elif book_choice== 5:
                    print(book_manager.get_all_books())
                elif book_choice== 6:
                    print(book_manager.delete_book())
                elif book_choice== 7:
                    print(book_manager.update_book())
                elif book_choice== 8:
                    print("Going to the main menu")
                    break
        elif choice==2:# manage users
            while True:
                user_choice=input_validator.choice_validator(1, 7, manage_users)
                if user_choice== 1:
                    print(user_manager.add_user())
                elif user_choice== 2:
                    print(user_manager.get_user_from_name())
                elif user_choice== 3:
                    print(user_manager.get_user_from_id())
                elif user_choice== 4:
                    print(user_manager.get_all_users())
                elif user_choice== 5:
                    print(user_manager.delete_user())
                elif user_choice== 6:
                    print(user_manager.update_user())
                elif user_choice== 7:
                    print("Going to the main menu")
                    break
        elif choice==3:# manage checks
            while True:# check menu
                check_choice=input_validator.choice_validator(1, 3, check_menu)
                if check_choice==1: # Checkin
                    user=user_manager.get_user_from_id()
                    if user=="User ID not found.":
                        print(user)
                        continue
                    else:
                        book=book_manager.get_book_from_isbn()
                        if book=="ISBN not found.":
                            print(book)
                            continue
                        if book["book_issue_flag"]:
                            print("Book already checked in")
                            continue
                    response=check_manager.check_in(user["user_id"], book["book_ISBN"])
                    if "success" in response:
                        book_manager.checkin(book["book_ISBN"])
                    print(response)
                elif check_choice==2: # Checkout
                    user=user_manager.get_user_from_id()
                    if user=="User ID not found.":
                        print(user)
                        continue
                    else:
                        book=book_manager.get_book_from_isbn()
                        if book=="ISBN not found.":
                            print(book)
                            continue
                    response=check_manager.check_out(user["user_id"], book["book_ISBN"])
                    if "success" in response:
                        book_manager.checkout(book["book_ISBN"])
                    print(response)
                elif check_choice==3:
                    break



        if choice==4:
            print("Exiting...")
            break
if __name__ == "__main__":
    main()
