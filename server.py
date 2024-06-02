import mysql.connector as mariaDB

def dbConnection():
    try:
        connection = mariaDB.connect(
            user='root',
            password='iamnicoantonio1124',
            host='localhost',  
            port=3306,         
            database='reviewsystemdb'  
        )
        return connection
    except mariaDB.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        return None

def signUp(f_name, m_name, l_name, birthday, email, password):
    connection = dbConnection()
    if connection is None:
        print("Failed to connect to the database.")
        return
    if checkEmailExists(email):
        print("Email already exists!")
        return
    try:
        cursor = connection.cursor()
        
        query = """
        INSERT INTO CUSTOMER (First_name, Middle_name, Last_name, Birthday, Age, Email, Password)
        VALUES (%s, %s, %s, STR_TO_DATE(%s, '%%m/%%d/%%Y'), 
        FLOOR(DATEDIFF(CURDATE(), STR_TO_DATE(%s, '%%m/%%d/%%Y')) / 365.25), %s, %s)
        """
        
        cursor.execute(query, (f_name, m_name, l_name, birthday, birthday, email, password))
        connection.commit()
        print("Signup successful!")
    
    except mariaDB.Error as e:
        print(f"Error: {e}")
    
    finally:
        cursor.close()
        connection.close()

def user_signIn(email, password):
    connection = dbConnection()
    if connection is None:
        print("Failed to connect to the database.")
        return 'db_error'
    
    try:
        cursor = connection.cursor()
        
        # Check if email exists
        email_query = """
        SELECT Email FROM CUSTOMER WHERE Email = %s
        """
        cursor.execute(email_query, (email,))
        email_rows = cursor.fetchall()
        
        if not email_rows:
            return 'email_not_found'
        
        # Check if password is correct
        query = """
        SELECT Email FROM CUSTOMER WHERE Email = %s AND Password = %s
        """
        cursor.execute(query, (email, password))
        rows = cursor.fetchall()
        
        if rows:
            return 'success'  # Sign-in successful
        else:
            return 'incorrect_password'  # Password incorrect
    
    except mariaDB.Error as e:
        print(f"Error: {e}")
        return 'db_error'
    
    finally:
        cursor.close()
        connection.close()

def admin_signIn(email, password):
    connection = dbConnection()
    if connection is None:
        print("Failed to connect to the database.")
        return 'db_error'
    
    try:
        cursor = connection.cursor()
        
        # Check if email exists
        email_query = """
        SELECT Email FROM ADMIN WHERE Email = %s
        """
        cursor.execute(email_query, (email,))
        email_rows = cursor.fetchall()
        
        if not email_rows:
            return 'email_not_found'
        
        # Check if password is correct
        query = """
        SELECT Email FROM ADMIN WHERE Email = %s AND Password = %s
        """
        cursor.execute(query, (email, password))
        rows = cursor.fetchall()
        
        if rows:
            return 'success'  # Sign-in successful
        else:
            return 'incorrect_password'  # Password incorrect
    
    except mariaDB.Error as e:
        print(f"Error: {e}")
        return 'db_error'
    
    finally:
        cursor.close()
        connection.close()

def checkEmailExists(email):
    connection = dbConnection()
    if connection is None:
        print("Failed to connect to the database.")
        return False
    
    try:
        cursor = connection.cursor()
        
        query = """
        SELECT Email FROM CUSTOMER WHERE Email = %s
        """
        
        cursor.execute(query, (email,))
        rows = cursor.fetchall()
        
        if rows:
            return True  # Email exists in the database
        else:
            return False  # Email does not exist in the database
    
    except mariaDB.Error as e:
        print(f"Error: {e}")
        return False
    
    finally:
        cursor.close()
        connection.close()



########## ADMIN FUNCTIONS ##########
def admin_signIn(email, password):
    connection = dbConnection()
    if connection is None:
        print("Failed to connect to the database.")
        return False
    
    try:
        cursor = connection.cursor()
        
        query = """
        SELECT email FROM ADMIN WHERE email = %s AND password = %s
        """
        
        cursor.execute(query, (email, password))
        rows = cursor.fetchall()
        
        if rows:
            print("Admin Sign In successful!")
            return True  # Sign-in successful
        else:
            print("Invalid email or password.")
            return False  # Sign-in failed
    
    except mariaDB.Error as e:
        print(f"Error: {e}")
        return False
    
    finally:
        cursor.close()
        connection.close()



########## FUNCTIONS FOR ADDING A FOOD ESTABLISHMENT ##########


#########################################################################################################
#                                                                                                       #
#                               Function for adding a food establishment                                #
#                                                                                                       #
#########################################################################################################
def addFoodEstablishment(name, barangay, postal_code, street_name, city, province, type_of_food_served, average_rating=0, price_range=0):
    connection = dbConnection()

    if connection is None:
        print("Failed to connect to database")
        return
    
    try:
        cursor = connection.cursor()

        query = """
        INSERT INTO FOOD_ESTABLISHMENT (name, barangay, postal_code, street_name, city, province, type_of_food_served, average_rating, price_range)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(query, (name, barangay, postal_code, street_name, city, province, type_of_food_served, average_rating, price_range))
        connection.commit()
        
        establishment_id = cursor.lastrowid  # Get the last inserted establishment ID
        
        # Compute and update the average price
        updateAveragePrice(establishment_id, cursor)
        
        # Compute and update the rating
        updateAverageRating(establishment_id, cursor)
        
        print("Food Establishment added successfully!")

    except mariaDB.Error as e:
        print(f"Error: {e}")
    
    finally:
        cursor.close()
        connection.close()

#########################################################################################################
#                                                                                                       #
#                               Function for updating a food establishment                             #
#                                                                                                       #
#########################################################################################################
def updateFoodEstablishment(establishment_id, name, barangay, postal_code, street_name, city, province, type_of_food_served):
    connection = dbConnection()
    if connection is None:
        print("Failed to connect to the database.")
        return
    
    try:
        cursor = connection.cursor()
        
        query = """
        UPDATE FOOD_ESTABLISHMENT
        SET name = %s, barangay = %s, postal_code = %s, street_name = %s, city = %s, province = %s, type_of_food_served = %s
        WHERE Establishment_id = %s
        """
        
        cursor.execute(query, (name, barangay, postal_code, street_name, city, province, type_of_food_served, establishment_id))
        connection.commit()
        
        # Compute and update the average price
        updateAveragePrice(establishment_id, cursor)
        
        # Compute and update the rating
        updateAverageRating(establishment_id, cursor)
        
        print("Food Establishment updated successfully!")
    
    except mariaDB.Error as e:
        print(f"Error: {e}")
    
    finally:
        cursor.close()
        connection.close()

#########################################################################################################
#                                                                                                       #
#                               Function for deleting a food establishment                              #
#                                                                                                       #
#########################################################################################################
def deleteFoodEstablishment(establishment_id):
    connection = dbConnection()
    if connection is None:
        print("Failed to connect to the database.")
        return
    
    try:
        cursor = connection.cursor()
        
        query = "DELETE FROM FOOD_ESTABLISHMENT WHERE Establishment_id = %s"
        
        cursor.execute(query, (establishment_id,))
        connection.commit()
        print("Food Establishment deleted successfully!")
    
    except mariaDB.Error as e:
        print(f"Error: {e}")
    
    finally:
        cursor.close()
        connection.close()

#########################################################################################################
#                                                                                                       #
#                               Function for searching a food establishment                             #
#                                                                                                       #
#########################################################################################################
def searchFoodEstablishment(search_term):
    connection = dbConnection()
    if connection is None:
        print("Failed to connect to the database.")
        return []
    
    try:
        cursor = connection.cursor()
        
        query = """
        SELECT * FROM FOOD_ESTABLISHMENT
        WHERE name LIKE %s OR city LIKE %s OR province LIKE %s
        """
        
        like_term = f"%{search_term}%"
        cursor.execute(query, (like_term, like_term, like_term))
        results = cursor.fetchall()
        
        return results
    
    except mariaDB.Error as e:
        print(f"Error: {e}")
        return []
    
    finally:
        cursor.close()
        connection.close()

#########################################################################################################
#                                                                                                       #
#               Function for getting the rating amd the average price of an establishment               #
#                                                                                                       #
#########################################################################################################
def updateAveragePrice(establishment_id, cursor):   
    try:
        query = """
        SELECT AVG(Price) FROM FOOD_ITEM WHERE Establishment_id = %s
        """
        cursor.execute(query, (establishment_id,))
        avg_price = cursor.fetchone()[0] or 0
        
        update_query = """
        UPDATE FOOD_ESTABLISHMENT SET price_range = %s WHERE Establishment_id = %s
        """
        cursor.execute(update_query, (avg_price, establishment_id))
    except mariaDB.Error as e:
        print(f"Error in updating average price: {e}")

def updateAverageRating(establishment_id, cursor):
    try:
        query = """
        SELECT AVG(Rating) FROM FOOD_REVIEW WHERE Establishment_id = %s
        """
        cursor.execute(query, (establishment_id,))
        average_rating = cursor.fetchone()[0] or 0
        
        update_query = """
        UPDATE FOOD_ESTABLISHMENT SET Rating = %s WHERE Establishment_id = %s
        """
        cursor.execute(update_query, (average_rating, establishment_id))
    except mariaDB.Error as e:
        print(f"Error in updating average rating: {e}")


#########################################################################################################
#                                                                                                       #
#                                Function for displaying the establishments                             #
#                                                                                                       #
#########################################################################################################
def get_all_food_establishments():
    connection = dbConnection()
    if connection is None:
        print("Failed to connect to the database.")
        return []
    
    try:
        cursor = connection.cursor()
        
        query = """
        SELECT * FROM FOOD_ESTABLISHMENT
        """
        
        cursor.execute(query)
        results = cursor.fetchall()
        
        return results
    
    except mariaDB.Error as e:
        print(f"Error: {e}")
        return []
    
    finally:
        cursor.close()
        connection.close()


#########################################################################################################
#                                                                                                       #
#                                   Function for adding the food item                                   #
#                                                                                                       #
#########################################################################################################
def addFoodItem(establishment_id, food_name, price, rating):
    connection = dbConnection()
    if connection is None:
        print("Failed to connect to the database.")
        return
    try:
        cursor = connection.cursor()
        
        query = """
        INSERT INTO FOOD_ITEM (Establishment_id, Food_name, Price, Rating)
        VALUES (%s, %s, %s, %s)
        """
        
        cursor.execute(query, (establishment_id, food_name, price, rating))
        connection.commit()
        print("Food Item added successfully!")
    
    except mariaDB.Error as e:
        print(f"Error: {e}")
    
    finally:
        cursor.close()
        connection.close()

def updateFoodItem(food_id, food_name, price, rating):
    connection = dbConnection()
    if connection is None:
        print("Failed to connect to the database.")
        return
    try:
        cursor = connection.cursor()
        
        query = """
        UPDATE FOOD_ITEM
        SET Food_name = %s, Price = %s, Rating = %s
        WHERE Food_id = %s
        """
        
        cursor.execute(query, (food_name, price, rating, food_id))
        connection.commit()
        print("Food Item updated successfully!")
    
    except mariaDB.Error as e:
        print(f"Error: {e}")
    
    finally:
        cursor.close()
        connection.close()

def deleteFoodItem(food_id):
    connection = dbConnection()
    if connection is None:
        print("Failed to connect to the database.")
        return
    try:
        cursor = connection.cursor()
        
        query = """
        DELETE FROM FOOD_ITEM
        WHERE Food_id = %s
        """
        
        cursor.execute(query, (food_id,))
        connection.commit()
        print("Food Item deleted successfully!")
    
    except mariaDB.Error as e:
        print(f"Error: {e}")
    
    finally:
        cursor.close()
        connection.close()

def searchFoodItem(search_term):
    connection = dbConnection()
    if connection is None:
        print("Failed to connect to the database.")
        return []
    try:
        cursor = connection.cursor()
        
        query = """
        SELECT * FROM FOOD_ITEM
        WHERE Food_name LIKE %s OR Price LIKE %s OR Rating LIKE %s
        """
        
        like_term = f"%{search_term}%"
        cursor.execute(query, (like_term, like_term, like_term))
        results = cursor.fetchall()
        
        return results
    
    except mariaDB.Error as e:
        print(f"Error: {e}")
        return []
    
    finally:
        cursor.close()
        connection.close()
