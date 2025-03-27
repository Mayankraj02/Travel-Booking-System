from database_travel import get_connection

def create_account():
    conn = get_connection()
    cursor = conn.cursor()

    phone_number = input('Phone Number: ')
    name = input('Name: ')
    password = input('Password (Max 10 chars): ')

    query = "INSERT INTO accounts (Phone_number, password, name) VALUES (%s, %s, %s)"
    cursor.execute(query, (phone_number, password, name))
    conn.commit()

    print('Account successfully created!')
    conn.close()

def login():
    conn = get_connection()
    cursor = conn.cursor()

    phone_number = input('Enter your phone number: ')

    query = "SELECT name, password FROM accounts WHERE phone_number = %s"
    cursor.execute(query, (phone_number,))
    result = cursor.fetchone()

    if not result:
        print("\n*********************** ACCOUNT DOESN'T EXIST ***********************\n")
        create_option = input("Press 32 to create an account or 0 to exit: ")
        if create_option == "32":
            create_account()
        return None

    name, correct_password = result

    password = input('Enter your password: ')
    if password != correct_password:
        print("\n*********************** INVALID PASSWORD ***********************\n")
        return None

    print(f"\nLOGGED IN! Welcome, {name}!\n")
    return phone_number  # Return the logged-in user's phone number

def delete_account():
    conn = get_connection()
    cursor = conn.cursor()

    phone_number = input("Enter your phone number to delete your account: ")

    cursor.execute("DELETE FROM customer_bookings WHERE phone_number = %s", (phone_number,))
    cursor.execute("DELETE FROM accounts WHERE phone_number = %s", (phone_number,))
    conn.commit()

    print("\n******************************** ACCOUNT SUCCESSFULLY DELETED ********************************\n")
    conn.close()
