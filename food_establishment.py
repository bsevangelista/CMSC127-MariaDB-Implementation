import server

def display_food_establishment():
    try:
        establishments = server.get_all_food_establishments()

        if establishments:
            print("----------- Food Establishments -----------")
            print("| Establishment ID | Name                | Barangay     | Postal Code | Street Name | City         | Province   | Food Type Served | Average Rating | Price Range |")
            print("-" * 116)

            for establishment in establishments:
                establishment_id, name, barangay, postal_code, street_name, city, province, food_type_served, average_rating, price_range = establishment
                print(f"| {establishment_id:<17} | {name:<20} | {barangay:<12} | {postal_code:<11} | {street_name:<12} | {city:<12} | {province:<10} | {food_type_served:<17} | {average_rating:<14} | {price_range:<11} |")

            print("-" * 116)
        else:
            print("No food establishments found.")
    except Exception as e:
        print(f"Error: {e}")

def add_food_establishment():
    try:
        name = input("Enter Establishment Name: ").strip()
        barangay = input("Enter Barangay: ").strip()
        postal_code = input("Enter Postal Code: ").strip()
        street_name = input("Enter Street Name: ").strip()
        city = input("Enter City: ").strip()
        province = input("Enter Province: ").strip()
        type_of_food_served = input("Enter Food Type Served: ").strip()

        # Set default values of average_rating and price_range to 0
        average_rating = 0
        price_range = 0

        server.addFoodEstablishment(name, barangay, postal_code, street_name, city, province, type_of_food_served, average_rating, price_range)
        print("Food Establishment added successfully!")
    except Exception as e:
        print(f"Error: {e}")


def update_food_establishment():
    try:
        establishment_id = input("Enter Establishment ID to update: ").strip()
        name = input("Enter new Establishment Name: ").strip()
        barangay = input("Enter new barangay: ").strip()
        postal_code = input("Enter new Postal Code: ").strip()
        street_name = input("Enter new street_name: ").strip()
        city = input("Enter new City: ").strip()
        province = input("Enter new Province: ").strip()
        type_of_food_served = input("Enter new Food Type Served: ").strip()

        server.updateFoodEstablishment(establishment_id, name, barangay, postal_code, street_name, city, province, type_of_food_served)
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
        elif choice == 5:
            print("Display Food Establishments selected.")
            display_food_establishment()
        else:
            print("Invalid option. Please try again.")
