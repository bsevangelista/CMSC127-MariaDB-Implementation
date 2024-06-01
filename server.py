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
