def home():
    while True:
        print("----------------Food Item-----------------")
        print("[1] Add Food Item")
        print("[2] Update Food Item")
        print("[3] Delete Food Item") 
        print("[4] Search Food Item") 
        print("[0] Back")
        
        choice = int(input("Select an option: "))
        
        if choice == 0:
            break
        elif choice == 1:
            print("Add Food Item selected.")
            # Add code to handle adding a review here
        elif choice == 2:
            print("Update Food Item selected.")
            # Add code to handle updating a review here
        elif choice == 3:
            print("Delete Food Item selected.")
            # Add code to handle deleting a review here
        elif choice == 4:
            print("Search Food Item selected.")
            # Add code to handle deleting a review here    
        else:
            print("Invalid option. Please try again.")
            