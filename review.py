import server

def get_customer_id(email):
    return server.getCustomerIdByEmail(email)

def get_all_establishment():
    return server.getFoodEstablishmentName()

# function for adding review
def add_review(customer_id):
    try:
        establishment_names = get_all_establishment()
        if establishment_names is False:
            print("Failed to retrieve food establishment names.")
            return
        elif establishment_names is None:
            print("No food establishments found.")
            return
        else:
            print("Food Establishment Names:")
            for name in establishment_names:
                print(name)
        
        # print(customer_id)
        # for testing only
        email = input("Enter your email: ").strip()
        test_id = get_customer_id(email)
        if not test_id:
            print("Customer not found. Try again!")
            return
        
    except Exception as e:
        print(e)



def home(customer_id):
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
            add_review(customer_id)
        elif choice == 2:
            print("Update Review selected.")
            # Add code to handle updating a review here
        elif choice == 3:
            print("Delete Review selected.")
            # Add code to handle deleting a review here
        else:
            print("Invalid option. Please try again.")
        
