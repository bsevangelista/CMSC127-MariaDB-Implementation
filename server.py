import mysql.connector as mariaDB

def dbConnection():
    try:
        connection = mariaDB.connect(
            user='root',
            password='admin',
            host='localhost',  
            port=3306,         
            database='FoodReviewDB'  
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
        VALUES (%s, %s, %s, %s, FLOOR(DATEDIFF(CURDATE(), %s) / 365.25), %s, %s)
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

# Function for adding a food establishment
def addFoodEstablishment(estab_name,
                         baranggay,
                         postal_code,
                         street,
                         city,
                         province,
                         rating, 
                         average_price, 
                         food_type_served):
    
    connection = dbConnection()

    if connection is None:
        print("Failed to connect to database")
        return
    
    try:
        cursor = connection.cursor()

        query = """
        INSERT INTO FOOD_ESTABLISHMENT (Estab_name, Baranggay, Postal_code, Street, City, Province, Rating, Average_price, Food_type_served)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(query,(estab_name,
                                baranggay,
                                postal_code,
                                street,
                                city,
                                province,
                                rating, 
                                average_price, 
                                food_type_served))
        
        connection.commit()
        print("Food Establishment added successfully!")

    except mariaDB.Error as e:
        print(f"Error: {e}")
    
    finally:
        cursor.close()
        connection.close()

# Function for updating food establishment
def updateFoodEstablishment(establishment_id, estab_name, baranggay, postal_code, street, city, province, rating, average_price, food_type_served):
    connection = dbConnection()
    if connection is None:
        print("Failed to connect to the database.")
        return
    
    try:
        cursor = connection.cursor()
        
        query = """
        UPDATE FOOD_ESTABLISHMENT
        SET Estab_name = %s, Baranggay = %s, Postal_code = %s, Street = %s, City = %s, Province = %s, Rating = %s, Average_price = %s, Food_type_served = %s
        WHERE Establishment_id = %s
        """
        
        cursor.execute(query, (estab_name, baranggay, postal_code, street, city, province, rating, average_price, food_type_served, establishment_id))
        connection.commit()
        print("Food Establishment updated successfully!")
    
    except mariaDB.Error as e:
        print(f"Error: {e}")
    
    finally:
        cursor.close()
        connection.close()

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

def searchFoodEstablishment(search_term):
    connection = dbConnection()
    if connection is None:
        print("Failed to connect to the database.")
        return []
    
    try:
        cursor = connection.cursor()
        
        query = """
        SELECT * FROM FOOD_ESTABLISHMENT
        WHERE Estab_name LIKE %s OR City LIKE %s OR Province LIKE %s
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

############## FOOD REVIEW FUNCTIONS ####################
def getFoodEstablishmentName():
    connection = dbConnection()
    if connection is None:
        print("Failed to connect to the database.")
        return False
    
    try:
        cursor = connection.cursor()
        
        query = """
        SELECT Estab_name FROM FOOD_ESTABLISHMENT
        """
        
        cursor.execute(query)
        results = cursor.fetchall()
        
        if results:
            return [row[0] for row in results]  # Extract names from the results
        else:
            return None 
    
    except mariaDB.Error as e:
        print(f"Error: {e}")
        return False
    
    finally:
        cursor.close()
        connection.close()
        
def getCustomerIdByEmail(email):
    connection = dbConnection()
    if connection is None:
        print("Failed to connect to the database.")
        return False
    
    try:
        cursor = connection.cursor()
        
        query = """
        SELECT Customer_id FROM CUSTOMER WHERE Email = %s
        """
        
        cursor.execute(query, (email,))
        result = cursor.fetchone()
        
        if result:
            return result[0]  # Extract names from the results
        else:
            return None 
    
    except mariaDB.Error as e:
        print(f"Error: {e}")
        return False
    
    finally:
        cursor.close()
        connection.close()