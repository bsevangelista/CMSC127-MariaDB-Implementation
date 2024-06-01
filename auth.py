import server
import re
import review
from datetime import datetime

def is_valid_email(email):
    # regex for validating an email address
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_regex, email) is not None

def is_valid_date(date_string):
    try:
        datetime.strptime(date_string, '%m/%d/%Y')
        return True
    except ValueError:
        return False

def user_signIn():
    while True:
        email = input('Email: ').strip()
        if not is_valid_email(email):
            print("Invalid email format.")
            continue
        break
    
    while True:
        password = input('Password: ').strip()
        if not len(password) >= 8:
            print("Password must be at least 8 characters long.")
            continue
        break
    
    if server.signIn(email, password):
        review.home()
        return
    return

def admin_signIn():
    while True:
        email = input('Email: ').strip()
        if not is_valid_email(email):
            print("Invalid email format.")
            continue
        break
    
    while True:
        password = input('Password: ').strip()
        if not len(password) >= 8:
            print("Password must be at least 8 characters long.")
            continue
        break
    
    if server.admin_signIn(email, password):
        # .admin_dashboard()
        return
    return

def signUp():
    while True:
        first_name = input('First Name: ').strip()
        if not first_name:
            print("First Name cannot be empty.")
            continue
        break
    while True:
        middle_name = input('Middle Name: ').strip()
        if not middle_name:
            print("Middle Name cannot be empty.")
            continue
        break
    
    while True:
        last_name = input('Last Name: ').strip()
        if not last_name:
            print("Last Name cannot be empty.")
            continue
        break
    
    while True:
        birthday = input('Birthday(mm/dd/yyyy): ').strip()
        if not is_valid_date(birthday):
            print("Invalid birthday format. Please use mm/dd/yyyy.")
            continue
        break
    
    while True:
        email = input('Email: ').strip()
        if not is_valid_email(email):
            print("Invalid email format.")
            continue
        break
    
    while True:
        password = input('Password: ').strip()
        if not len(password) >= 8:
            print("Password must be at least 8 characters long.")
            continue
        break
    
    server.signUp(first_name, middle_name, last_name, birthday, email, password)
    return

## start loop
def start():
    while True:
        print("------------------Welcome-----------------")
        print("[1] User Sign In")
        print("[2] Admin Sign In")
        print("[3] Sign Up")
        print("[0] Exit")
        
        choice = int(input("Select an option: "))
        
        if choice == 0:
            print("Goodbye!")
            break
        elif choice == 1:
            user_signIn()
        elif choice == 2:
            admin_signIn()
        elif choice == 3:
            signUp()
        else:
            print("Invalid option. Please try again.")