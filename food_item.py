import server

def add_food_item():
    try:
        establishment_id = input("Enter Establishment ID: ").strip()
        
        # Check if the establishment exists
        if not server.isEstablishmentExists(establishment_id):
            print("Establishment ID does not exist. Please enter a valid Establishment ID.")
            return
        
        name = input("Enter Food Name: ").strip()
        price = input("Enter Price: ").strip()
        description = input("Enter Food Description: ").strip()

        server.addFoodItem(establishment_id, name, price, description)
        print("Food Item added successfully!")
    except Exception as e:
        print(f"Error: {e}")

def update_food_item():
    try:
        food_id = input("Enter Food ID to update: ").strip()
        food_name = input("Enter new Food Name: ").strip()
        price = input("Enter new Price: ").strip()

        server.updateFoodItem(food_id, food_name, price)
        print("Food Item updated successfully!")
    except Exception as e:
        print(f"Error: {e}")

def delete_food_item():
    try:
        food_id = input("Enter Food ID to delete: ").strip()
        server.deleteFoodItem(food_id)
        print("Food Item deleted successfully!")
    except Exception as e:
        print(f"Error: {e}")

def search_food_item():
    try:
        search_term = input("Enter search term (name, price, etc.): ").strip()
        results = server.searchFoodItem(search_term)
        
        if results:
            for result in results:
                print(result)
        else:
            print("No matching food items found.")
    except Exception as e:
        print(f"Error: {e}")

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
            add_food_item()
        elif choice == 2:
            print("Update Food Item selected.")
            update_food_item()
        elif choice == 3:
            print("Delete Food Item selected.")
            delete_food_item()
        elif choice == 4:
            print("Search Food Item selected.")
            search_food_item()    
        else:
            print("Invalid option. Please try again.")
