import server

def get_customer_id(email):
    return server.getCustomerIdByEmail(email)

# function for adding review
def add_review():

    try:

        email = input("Enter your email: ").strip()
        customer_id = get_customer_id(email)

        if not customer_id:
            print("Customer not found. Try again!")
            return
               

    
    except Exception as e:
        print(e)



def home():
    while True:
        print("------------------Review------------------")
        print("[1] Add Review")
        print("[2] Update Review")
        print("[3] Delete Review") 
        print("[0] Back")
        
        choice = int(input("Select an option: "))
        
        if choice == 0:
            break
        elif choice == 1:
            print("Add Review selected.")
            # Add code to handle adding a review here
        elif choice == 2:
            print("Update Review selected.")
            # Add code to handle updating a review here
        elif choice == 3:
            print("Delete Review selected.")
            # Add code to handle deleting a review here
        else:
            print("Invalid option. Please try again.")
            