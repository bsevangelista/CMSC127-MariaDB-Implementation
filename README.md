# CMSC127-MariaDB-Implementation
# Banzon-Evangelista-Montero

# Food Review Application in Python

This application allows users to review food establishments and food items. It uses Python and MariaDB for database management. Follow the instructions below to set up and run the application on your device.

## Prerequisites

Before you start, ensure you have the following installed on your device:

- Python (version 3.6 or higher)
- MariaDB

## Installation

### Step 1: Install Python

1. Download the Python installer from the [official Python website](https://www.python.org/downloads/).
2. Run the installer and follow the instructions. Make sure to check the option to add Python to your PATH.

### Step 2: Install MariaDB

1. Download the MariaDB installer from the [official MariaDB website](https://mariadb.org/download/).
2. Run the installer and follow the instructions to set up MariaDB on your device.

### Step 3: Install Required Python Packages

Open a command prompt or terminal and run the following command to install the required Python package:

python -m pip install -U prettytable

### Step 4: Import the SQL Schema

Import the review.sql in MariaDB

### Step 5: Configure the Database Connection

Open the server.py file in a text editor.
Locate the dbConnection function and edit the connection parameters to match your MariaDB setup:

def dbConnection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='your_username',
            password='your_password',
            database='FoodReviewDB'
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

Replace your_username and your_password with your actual MariaDB username and password.

### Step 5:Running the Application
run

python main.py

in the terminal