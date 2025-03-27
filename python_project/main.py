import sys
from account import create_account, login, delete_account
from coustemer_detail import book_trip, generate_bill, view_travel_log

def main():
    print("\n********** TRAVEL DAILY WELCOMES YOU! **********\n")
    
    print("1. Login")
    print("2. Create Account")
    print("3. Delete Account")
    print("4. Exit\n")

    choice = input("Enter your choice: ")

    if choice == "1":
        phone_number = login()
        if phone_number:
            while True:
                print("\n1. Book a Ride")
                print("2. Bill Verification")
                print("3. My Travel Log")
                print("4. Logout\n")

                user_choice = input("Enter your choice: ")

                if user_choice == "1":
                    book_trip(phone_number)
                elif user_choice == "2":
                    generate_bill()
                elif user_choice == "3":
                    view_travel_log(phone_number)
                elif user_choice == "4":
                    print("\nThank you! Visit again!\n")
                    sys.exit()
                else:
                    print("\nInvalid choice! Try again.\n")

    elif choice == "2":
        create_account()
    elif choice == "3":
        delete_account()
    elif choice == "4":
        sys.exit()
    else:
        print("\nInvalid choice! Please try again.\n")
        main()

if __name__ == "__main__":
    main()
