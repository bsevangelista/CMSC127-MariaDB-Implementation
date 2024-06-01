import mysql.connector as mariaDB

# configure before using to other devices
def dbConnection():
    try:
        connection = mariaDB.connect(
            user='root',
            password='admin',
            host='localhost',  
            port=3306,         
            database='test'  
        )
        return connection
    except mariaDB.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        return None

######################################## INSERT FUNCTIONS #################################################
def signUp(f_name, m_name, l_name, birthday, email, password):
    connection = dbConnection()
    if connection is None:
        print("Failed to connect to the database.")
        return
    if checkEmailExists(email):
        print("Email already existing!")
        return
    try:
        cursor = connection.cursor()
        
        query = """
        INSERT INTO customer (first_name, middle_name, last_name, birthday, age, email, password)
        VALUES (%s, %s, %s, STR_TO_DATE(%s, '%m/%d/%Y'), 
        FLOOR(DATEDIFF(CURDATE(), STR_TO_DATE(%s, '%m/%d/%Y')) / 365.25), %s, %s)
        """
        
        cursor.execute(query, (f_name, m_name, l_name, birthday, birthday, email, password))
        connection.commit()
        print("Signup successful!")
    
    except mariaDB.Error as e:
        print(f"Error: {e}")
    
    finally:
        cursor.close()
        connection.close()

######################################## SELECT FUNCTIONS #################################################
def signIn(email, password):
    connection = dbConnection()
    if connection is None:
        print("Failed to connect to the database.")
        return
    
    try:
        cursor = connection.cursor()
        
        query = """
        SELECT email FROM customer WHERE email = %s AND password = %s
        """
        
        cursor.execute(query, (email, password))
        rows = cursor.fetchall()
        
        if rows:
            print("Signin successful!")
            return True  # Sign-in successful
        else:
            print("Invalid email or password.")
            return False  # Sign-in failed
    
    except mariaDB.Error as e:
        print(f"Error: {e}")
    
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
        SELECT email FROM customer WHERE email = %s
        """
        
        cursor.execute(query, (email,))
        rows = cursor.fetchall()
        # print(rows)
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
        

# print(dbConnection())
# signUp('John', 'M', 'Doe', '01/01/1990', 'john.doe@example.com', 'password123')