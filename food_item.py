import server

def show_all_establishments():
    establishments = server.getAllEstablishments()
    if establishments:
        print("\nList of Establishments:")
        print("-" * 45)
        for establishment in establishments:
            print("{:<15} {:<30}".format("["+str(establishment[0])+"]", establishment[1]))
        print("-" * 45)
    else:
        print("No establishments found.")
        return("No establishments found.")
    
def show_all_food_items():
    food_items = server.getAllFoodItems()
    if food_items:
        print("\nList of Food Items:")
        print("-" * 40)
        for food_item in food_items:
            print("{:<10} {:<30}".format(food_item[0], food_item[1]))
        print("-" * 40)
    else:
        print("No food items found.")
        return("No food items found.")

def add_food_item():
    try:
        show_all_establishments()
        establishment_id = input("Enter Establishment ID: ").strip()
        
        # Check if the establishment exists
        if not server.isEstablishmentExists(establishment_id):
            print("Establishment ID does not exist. Please enter a valid Establishment ID.")
            return
        
        print("Select Food Type:")
        print("[1] Meat")
        print("[2] Vegetable")
        print("[3] Dessert")
        food_type_choice = input("Enter choice (1, 2, or 3): ").strip()
        
        food_type = None
        if food_type_choice == '1':
            food_type = 'Meat'
            specific_type = input("Enter Meat Type: ").strip()
        elif food_type_choice == '2':
            food_type = 'Vegetable'
            specific_type = input("Enter Vegetable Type: ").strip()
        elif food_type_choice == '3':
            food_type = 'Dessert'
            specific_type = input("Enter Dessert Type: ").strip()
        else:
            print("Invalid choice. Please enter a valid option.")
            return
        
        name = input("Enter Food Name: ").strip()
        price = input("Enter Price: ").strip()
        description = input("Enter Food Description: ").strip()

        server.addFoodItem(establishment_id, name, price, description, food_type, specific_type)
    except Exception as e:
        print(f"Error: {e}")

def update_food_item():
    try:
        show_all_food_items()
        food_id = input("Enter Food ID to update: ").strip()
        name = input("Enter new Food Name: ").strip()
        price = input("Enter new Price: ").strip()

        server.updateFoodItem(food_id, name, price)
    except Exception as e:
        print(f"Error: {e}")

def delete_food_item():
    try:
        show_all_food_items()
        food_id = input("Enter Food ID to delete: ").strip()
        server.deleteFoodItem(food_id)
    except Exception as e:
        print(f"Error: {e}")

def search_food_item():
    try:
        search_term = input("Enter search term - [NAME][PROVINCE][CITY][STREET][BARANGAY][POSTAL CODE]:").strip()
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
        
        try:
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
        except ValueError:
            print("Invalid input. Please enter a number.")