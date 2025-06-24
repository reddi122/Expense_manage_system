# main.py

from new_user import register_user
from existing_user import (
    login_user, add_expense, view_expenses,
    delete_expense, modify_expense, report_expenses
)

def expense_menu(username):
    while True:
        print("\n1. Add\n2. Delete\n3. Modify\n4. View\n5. Report\n6. Logout")
        choice = input("Choose: ")
        if choice == "1":
            add_expense(username)
        elif choice == "2":
            delete_expense(username)
        elif choice == "3":
            modify_expense(username)
        elif choice == "4":
            view_expenses(username)
        elif choice == "5":
            report_expenses(username)
        elif choice == "6":
            print("Logged out.")
            break
        else:
            print("Invalid option.")

def main():
    while True:
        print("\n1. Register\n2. Login\n3. Quit")
        option = input("Choose: ")
        if option == "1":
            user = register_user()
            expense_menu(user)
        elif option == "2":
            user = login_user()
            if user:
                expense_menu(user)
        elif option == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
