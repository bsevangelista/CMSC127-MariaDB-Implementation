import food_establishment
import food_item

def home():
    while True:
        print("--------------Admin Dashboard-------------")
        print("[1] Food Item")
        print("[2] Food Establishment")
        print("[0] Exit")
        
        choice = input("Select an option: ").strip()
        
        if choice == "0":
            print("Goodbye!")
            break
        elif choice == "1":
            food_item.home()
        elif choice == "2":
            food_establishment.home()
        else:
            print("Invalid option. Please try again.")
            
            