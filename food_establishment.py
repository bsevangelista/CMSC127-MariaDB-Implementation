def home():
    while True:
        print("------------Food Establishment------------")
        print("[1] Add Food Establishment")
        print("[2] Update Food Establishment")
        print("[3] Delete Food Establishment") 
        print("[4] Search Food Establishment") 
        print("[0] Back")
        
        choice = int(input("Select an option: "))
        
        if choice == 0:
            break
        elif choice == 1:
            print("Add Food Establishment selected.")
            # Add code to handle adding a review here
        elif choice == 2:
            print("Update Food Establishment selected.")
            # Add code to handle updating a review here
        elif choice == 3:
            print("Delete Food Establishment selected.")
            # Add code to handle deleting a review here
        elif choice == 4:
            print("Search Food Establishment selected.")
            # Add code to handle deleting a review here    
        else:
            print("Invalid option. Please try again.")
            