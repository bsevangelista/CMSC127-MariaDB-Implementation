import food_establishment  # Import the module for managing food establishments
import food_item  # Import the module for managing food items

def admin_menu():
    while True:
        print("------------Admin Menu------------")
        print("[1] Manage Food Establishments")
        print("[2] Manage Food Items")
        print("[0] Logout")
        
        choice = input("Select an option: ")
        
        if choice == '0':
            print("Logging out...")
            break
        elif choice == '1':
            food_establishment.home()  # Redirect to the food establishment management menu
        elif choice == '2':
            food_item.home()  # Redirect to the food item management menu
        else:
            print("Invalid option. Please try again.")
