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
        INSERT INTO CUSTOMER (first_name, middle_name, last_name, birthday, age, email, password)
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
        SELECT email FROM CUSTOMER WHERE email = %s
        """
        cursor.execute(email_query, (email,))
        email_rows = cursor.fetchall()
        
        if not email_rows:
            return 'email_not_found'
        
        # Check if password is correct
        query = """
        SELECT email FROM CUSTOMER WHERE email = %s AND password = %s
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
        SELECT email FROM ADMIN WHERE email = %s
        """
        cursor.execute(email_query, (email,))
        email_rows = cursor.fetchall()
        
        if not email_rows:
            return 'email_not_found'
        
        # Check if password is correct
        query = """
        SELECT email FROM ADMIN WHERE email = %s AND password = %s
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
        SELECT email FROM CUSTOMER WHERE email = %s
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


#########################################################################################################
#                               Function for adding a food establishment                                #
#########################################################################################################
def addFoodEstablishment(name, barangay, postal_code, street_name, city, province, type_of_food_served, average_rating=0, average_price=0):
    connection = dbConnection()

    if connection is None:
        print("Failed to connect to database")
        return
    
    try:
        cursor = connection.cursor()

        query = """
        INSERT INTO FOOD_ESTABLISHMENT (name, barangay, postal_code, street_name, city, province, type_of_food_served, average_rating, average_price)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(query, (name, barangay, postal_code, street_name, city, province, type_of_food_served, average_rating, average_price))
        connection.commit()
        
        print("Food Establishment added successfully!")

    except mariaDB.Error as e:
        print(f"Error: {e}")
    
    finally:
        cursor.close()
        connection.close()

#########################################################################################################
#                               Function for updating a food establishment                             #
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
#                               Function for deleting a food establishment                              #
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
#                               Function for searching a food establishment                             #
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
#                       Function for getting the average price of an establishment                      #
#########################################################################################################
def updateAveragePrice(establishment_id, cursor):
    try:
        # Update the average price in the FOOD_ESTABLISHMENT table
        update_query = """
        UPDATE FOOD_ESTABLISHMENT 
        SET average_price = (SELECT AVG(price) FROM FOOD_ITEM WHERE establishment_id = %s) 
        WHERE establishment_id = %s
        """
        cursor.execute(update_query, (establishment_id, establishment_id))
        
        # Fetch the updated average price to verify the update
        cursor.execute("SELECT average_price FROM FOOD_ESTABLISHMENT WHERE Establishment_id = %s", (establishment_id,))
        updated_avg_price = cursor.fetchone()[0]
        
        print(f"The updated average price for establishment ID {establishment_id} is {updated_avg_price}")
    except mariaDB.Error as e:
        print(f"Error in updating average price: {e}")

#########################################################################################################
#                                Function for displaying the establishments                             #
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
#                                Function for checking if establishment exists                          #
#########################################################################################################
def isEstablishmentExists(establishment_id):
    connection = dbConnection()
    if connection is None:
        print("Failed to connect to the database.")
        return False
    
    try:
        cursor = connection.cursor()
        query = "SELECT COUNT(*) FROM FOOD_ESTABLISHMENT WHERE Establishment_id = %s"
        cursor.execute(query, (establishment_id,))
        result = cursor.fetchone()
        
        return result[0] > 0  # Returns True if establishment exists, otherwise False
    except mariaDB.Error as e:
        print(f"Error: {e}")
        return False
    finally:
        cursor.close()
        connection.close()


#########################################################################################################
#                                   Function for adding the food item                                   #
#########################################################################################################
def addFoodItem(establishment_id, name, price, description):
    connection = dbConnection()
    if connection is None:
        print("Failed to connect to the database.")
        return
    
    try:
        cursor = connection.cursor()

        # Insert the new food item
        query = """
        INSERT INTO FOOD_ITEM (establishment_id, name, price, description)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (establishment_id, name, price, description))

        # Update the average price after adding a new food item
        updateAveragePrice(establishment_id, cursor)

        connection.commit()  # Commit the transaction here
    
        print("Food Item added successfully!")
    
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

        # Get the establishment_id for the food item
        cursor.execute("SELECT establishment_id FROM FOOD_ITEM WHERE Food_id = %s", (food_id,))
        establishment_id = cursor.fetchone()[0]
        
        # Delete the food item
        query = "DELETE FROM FOOD_ITEM WHERE Food_id = %s"
        cursor.execute(query, (food_id,))
        
        # Update the average price
        updateAveragePrice(establishment_id, cursor)
        
        connection.commit()
        print("Food Item deleted successfully!")
    
    except mariaDB.Error as e:
        print(f"Error: {e}")
    
    finally:
        cursor.close()
        connection.close()

def updateFoodItem(food_id, name, price):
    connection = dbConnection()
    if connection is None:
        print("Failed to connect to the database.")
        return
    
    try:
        cursor = connection.cursor()
        
        query = """
        UPDATE FOOD_ITEM
        SET name = %s, price = %s
        WHERE Food_id = %s
        """
        
        cursor.execute(query, (name, price, food_id))

        # Get the establishment_id for the food item
        cursor.execute("SELECT establishment_id FROM FOOD_ITEM WHERE Food_id = %s", (food_id,))
        establishment_id = cursor.fetchone()[0]
        
        # Update the average price
        updateAveragePrice(establishment_id, cursor)
        
        connection.commit()
        print("Food Item updated successfully!")
    
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
        WHERE name LIKE %s OR Price LIKE %s OR Rating LIKE %s
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
#                               FOOD REVIEW FUNCTIONS                                                   #
#                                                                                                       #
#########################################################################################################
def getFoodEstablishmentName():
    connection = dbConnection()
    if connection is None:
        print("Failed to connect to the database.")
        return False
    
    try:
        cursor = connection.cursor()
        
        query = """
        SELECT name FROM FOOD_ESTABLISHMENT
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

def getFoodItemsByEstabId(establishment_id):
    connection = dbConnection()
    if connection is None:
        print("Failed to connect to the database.")
        return False
    
    try:
        cursor = connection.cursor()
        
        query = """
        SELECT name FROM FOOD_ITEM WHERE establishment_id = %s
        """
        
        cursor.execute(query, (establishment_id,))
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
        SELECT customer_id FROM CUSTOMER WHERE email = %s
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
        
def getEstablishmentIdByName(establishmment_name):
    connection = dbConnection()
    if connection is None:
        print("Failed to connect to the database.")
        return False
    
    try:
        cursor = connection.cursor()
        
        query = """
        SELECT establishment_id FROM FOOD_ESTABLISHMENT WHERE name = %s
        """
        
        cursor.execute(query, (establishmment_name,))
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
        
def getItemIdByName(item_name, establishment_id):
    connection = dbConnection()
    if connection is None:
        print("Failed to connect to the database.")
        return False
    
    try:
        cursor = connection.cursor()
        
        query = """
        SELECT food_id FROM FOOD_ITEM WHERE name = %s AND establishment_id = %s
        """
        
        cursor.execute(query, (item_name, establishment_id))
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
        
# ADD FOOD_ESTABLISHMENT REVIEW
def addFoodEstablishmentReview(type, title, suggestion, rating, customer_id, establishment_id):
    connection = dbConnection()
    if connection is None:
        print("Failed to connect to the database.")
        return
    
    try:
        cursor = connection.cursor()
        
        query = """
        INSERT INTO FOOD_REVIEW (review_date, review_time, Type_of_review, rating, title, suggestion, customer_id, establishment_id)
        VALUES (CURDATE(), CURTIME(), %s, %s, %s, %s, %s, %s)
        """
        
        cursor.execute(query, (type, rating, title, suggestion, customer_id, establishment_id))
        updateAverageRating(establishment_id, cursor)
        
        connection.commit()
        print("Review Added successfully!")
    
    except mariaDB.Error as e:
        print(f"Error: {e}")
    
    finally:
        cursor.close()
        connection.close()



# AVERAGE THE FOOD_ESTABLISHMENT REVIEW
def updateAverageRating(establishment_id, cursor):
    try:
        # Update the average rating in the FOOD_ESTABLISHMENT table
        update_query = """
        UPDATE FOOD_ESTABLISHMENT 
        SET average_rating = (SELECT AVG(rating) FROM FOOD_REVIEW WHERE establishment_id = %s) 
        WHERE establishment_id = %s
        """
        cursor.execute(update_query, (establishment_id, establishment_id))
        
        # Fetch the updated average rating to verify the update
        cursor.execute("SELECT average_rating FROM FOOD_ESTABLISHMENT WHERE establishment_id = %s", (establishment_id,))
        updated_avg_rating = cursor.fetchone()[0]
        
        print(f"The updated average rating for establishment ID {establishment_id} is {updated_avg_rating}")
    except mariaDB.Error as e:
        print(f"Error in updating average rating: {e}")


def addFoodItemReview(type, title, suggestion, rating, customer_id, establishment_id, item_id):
        connection = dbConnection()
        if connection is None:
            print("Failed to connect to the database.")
            return
        
        try:
            cursor = connection.cursor()
            
            query = """
            INSERT INTO FOOD_REVIEW (review_date, review_time, Type_of_review, rating, title, suggestion, customer_id, establishment_id, food_id)
            VALUES (CURDATE(), CURTIME(), %s, %s, %s, %s, %s, %s, %s)
            """
            
            cursor.execute(query, (type, rating, title, suggestion, customer_id, establishment_id, item_id))
            connection.commit()
            print("Review Added successfully!")
        
        except mariaDB.Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            connection.close()
            
def getReviewsByCustomerId(customer_id):
    connection = dbConnection()
    if connection is None:
        print("Failed to connect to the database.")
        return False
    
    try:
        cursor = connection.cursor()
        
        query = """
        SELECT 
            r.review_id,
            r.title,
            r.suggestion,
            r.rating,
            fi.name as item_name,
            fe.name as establishment_name
        FROM 
            FOOD_REVIEW r
        JOIN 
            CUSTOMER c ON r.customer_id = c.customer_id
        LEFT JOIN 
            FOOD_ITEM fi ON r.food_id = fi.food_id
        LEFT JOIN 
            FOOD_ESTABLISHMENT fe ON r.establishment_id = fe.establishment_id
        WHERE 
            r.customer_id = %s
        """
        
        cursor.execute(query, (customer_id,))
        results = cursor.fetchall()
        
        if results:
            return results
        else:
            return None 
    
    except mariaDB.Error as e:
        print(f"Error: {e}")
        return False
    
    finally:
        cursor.close()
        connection.close()
        
def getReviewByReviewId(review_id):
    connection = dbConnection()
    if connection is None:
        print("Failed to connect to the database.")
        return False
    
    try:
        cursor = connection.cursor()
        
        query = """
        SELECT * FROM FOOD_REVIEW WHERE review_id = %s
        """
        
        cursor.execute(query, (review_id,))
        result = cursor.fetchone()
        
        if result:
            return result  
        else:
            return None 
    
    except mariaDB.Error as e:
        print(f"Error: {e}")
        return False
    
    finally:
        cursor.close()
        connection.close()
        
def updateReview(review_id, title, suggestion, rating):
    connection = dbConnection()
    if connection is None:
        print("Failed to connect to the database.")
        return False
    
    try:
        cursor = connection.cursor()
        
        query = """
        UPDATE FOOD_REVIEW 
        SET title = %s, suggestion = %s, rating = %s 
        WHERE review_id = %s
        """
        
        cursor.execute(query, (title, suggestion, rating, review_id))
        connection.commit()
        print("Review updated successfully.")
        return True
    
    except mariaDB.Error as e:
        print(f"Error: {e}")
        return False
    
    finally:
        cursor.close()
        connection.close()

def deleteReview(review_id):
    connection = dbConnection()
    if connection is None:
        print("Failed to connect to the database.")
        return False
    
    try:
        cursor = connection.cursor()
        
        query = """
        DELETE FROM FOOD_REVIEW 
        WHERE review_id = %s
        """
        
        cursor.execute(query, (review_id,))
        connection.commit()
        print("Review deleted successfully.")
        return True
    
    except mariaDB.Error as e:
        print(f"Error: {e}")
        return False
    
    finally:
        cursor.close()
        connection.close()


