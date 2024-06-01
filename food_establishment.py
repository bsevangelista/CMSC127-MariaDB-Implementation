import server

def add_food_establishment():
    try:
        estab_name = input("Enter Establishment Name: ").strip()
        baranggay = input("Enter Baranggay: ").strip()
        postal_code = input("Enter Postal Code: ").strip()
        street = input("Enter Street: ").strip()
        city = input("Enter City: ").strip()
        province = input("Enter Province: ").strip()
        rating = input("Enter Rating (1-5): ").strip()
        average_price = input("Enter Average Price: ").strip()
        food_type_served = input("Enter Food Type Served: ").strip()

        server.addFoodEstablishment(estab_name, baranggay, postal_code, street, city, province, rating, average_price, food_type_served)
        print("Food Establishment added successfully!")
    except Exception as e:
        print(f"Error: {e}")

def update_food_establishment():
    try:
        establishment_id = input("Enter Establishment ID to update: ").strip()
        estab_name = input("Enter new Establishment Name: ").strip()
        baranggay = input("Enter new Baranggay: ").strip()
        postal_code = input("Enter new Postal Code: ").strip()
        street = input("Enter new Street: ").strip()
        city = input("Enter new City: ").strip()
        province = input("Enter new Province: ").strip()
        rating = input("Enter new Rating (1-5): ").strip()
        average_price = input("Enter new Average Price: ").strip()
        food_type_served = input("Enter new Food Type Served: ").strip()

        server.updateFoodEstablishment(establishment_id, estab_name, baranggay, postal_code, street, city, province, rating, average_price, food_type_served)
        print("Food Establishment updated successfully!")
    except Exception as e:
        print(f"Error: {e}")

def delete_food_establishment():
    try:
        establishment_id = input("Enter Establishment ID to delete: ").strip()
        server.deleteFoodEstablishment(establishment_id)
        print("Food Establishment deleted successfully!")
    except Exception as e:
        print(f"Error: {e}")

def search_food_establishment():
    try:
        search_term = input("Enter search term (name, city, etc.): ").strip()
        results = server.searchFoodEstablishment(search_term)
        
        if results:
            for result in results:
                print(result)
        else:
            print("No matching establishments found.")
    except Exception as e:
        print(f"Error: {e}")

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
            add_food_establishment()
        elif choice == 2:
            print("Update Food Establishment selected.")
            update_food_establishment()
        elif choice == 3:
            print("Delete Food Establishment selected.")
            delete_food_establishment()
        elif choice == 4:
            print("Search Food Establishment selected.")
            search_food_establishment()    
        else:
            print("Invalid option. Please try again.")
