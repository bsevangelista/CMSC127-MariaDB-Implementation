CREATE DATABASE FoodReviewDB;
USE FoodReviewDB;

-- Table for CUSTOMER
CREATE TABLE CUSTOMER (
    Customer_id INT AUTO_INCREMENT PRIMARY KEY,
    First_name VARCHAR(50),
    Middle_name VARCHAR(50),
    Last_name VARCHAR(50),
    Birthday DATE,
    Age INT,
    Email VARCHAR(100),
    Password VARCHAR(100)
);

-- Table for FOOD_ESTABLISHMENT
CREATE TABLE FOOD_ESTABLISHMENT (
    Establishment_id INT AUTO_INCREMENT PRIMARY KEY,
    Estab_name VARCHAR(100),
    Baranggay VARCHAR(100),
    Postal_code VARCHAR(10),
    Street VARCHAR(100),
    City VARCHAR(50),
    Province VARCHAR(50),
    Rating FLOAT DEFAULT 0, -- Initial value set to 0
    Average_price FLOAT DEFAULT 0, -- Initial value set to 0
    food_type_served VARCHAR(100)
);


-- Table for FOOD_ITEM
CREATE TABLE FOOD_ITEM (
    Food_id INT AUTO_INCREMENT PRIMARY KEY,
    Price FLOAT,
    Rating FLOAT,
    Food_name VARCHAR(100),
    Establishment_id INT,
    FOREIGN KEY (Establishment_id) REFERENCES FOOD_ESTABLISHMENT(Establishment_id)
);

-- Table for FOOD_REVIEW
CREATE TABLE FOOD_REVIEW (
    Review_id INT AUTO_INCREMENT PRIMARY KEY,
    Date_of_review DATE,
    Type_of_review VARCHAR(100),
    Rating INT,
    Title VARCHAR(100),
    Suggestion TEXT,
    Customer_id INT,
    Establishment_id INT,
    Food_id INT,
    FOREIGN KEY (Customer_id) REFERENCES CUSTOMER(Customer_id),
    FOREIGN KEY (Establishment_id) REFERENCES FOOD_ESTABLISHMENT(Establishment_id),
    FOREIGN KEY (Food_id) REFERENCES FOOD_ITEM(Food_id)
);

-- Table for FOOD_ITEM_INGREDIENT
CREATE TABLE FOOD_ITEM_INGREDIENT (
    Food_id INT,
    Ingredient VARCHAR(100),
    FOREIGN KEY (Food_id) REFERENCES FOOD_ITEM(Food_id),
    PRIMARY KEY (Food_id, Ingredient)
);

-- Table for MEA
CREATE TABLE MEA (
    Food_id INT,
    Meat_type VARCHAR(50),
    FOREIGN KEY (Food_id) REFERENCES FOOD_ITEM(Food_id),
    PRIMARY KEY (Food_id, Meat_type)
);

-- Table for VEGETABLE
CREATE TABLE VEGETABLE (
    Food_id INT,
    Vegetable_type VARCHAR(50),
    FOREIGN KEY (Food_id) REFERENCES FOOD_ITEM(Food_id),
    PRIMARY KEY (Food_id, Vegetable_type)
);

-- Table for DESSERT
CREATE TABLE DESSERT (
    Food_id INT,
    Dessert_type VARCHAR(50),
    FOREIGN KEY (Food_id) REFERENCES FOOD_ITEM(Food_id),
    PRIMARY KEY (Food_id, Dessert_type)
);

-- Trigger to update the average price in FOOD_ESTABLISHMENT when a FOOD_ITEM is inserted
DELIMITER //
CREATE TRIGGER update_average_price
AFTER INSERT ON FOOD_ITEM
FOR EACH ROW
BEGIN
    DECLARE avg_price FLOAT;
    SELECT AVG(Price) INTO avg_price FROM FOOD_ITEM WHERE Establishment_id = NEW.Establishment_id;
    UPDATE FOOD_ESTABLISHMENT SET Average_price = avg_price WHERE Establishment_id = NEW.Establishment_id;
END;
//
DELIMITER ;

-- Trigger to update the average price in FOOD_ESTABLISHMENT when a FOOD_ITEM is updated
DELIMITER //
CREATE TRIGGER update_average_price_on_update
AFTER UPDATE ON FOOD_ITEM
FOR EACH ROW
BEGIN
    DECLARE avg_price FLOAT;
    SELECT AVG(Price) INTO avg_price FROM FOOD_ITEM WHERE Establishment_id = OLD.Establishment_id;
    UPDATE FOOD_ESTABLISHMENT SET Average_price = avg_price WHERE Establishment_id = OLD.Establishment_id;
END;
//
DELIMITER ;

-- Trigger to update the average rating in FOOD_ESTABLISHMENT when a FOOD_REVIEW is inserted
DELIMITER //
CREATE TRIGGER update_average_rating
AFTER INSERT ON FOOD_REVIEW
FOR EACH ROW
BEGIN
    DECLARE avg_rating FLOAT;
    SELECT AVG(Rating) INTO avg_rating FROM FOOD_REVIEW WHERE Establishment_id = NEW.Establishment_id;
    UPDATE FOOD_ESTABLISHMENT SET Rating = avg_rating WHERE Establishment_id = NEW.Establishment_id;
END;
//
DELIMITER ;

-- Trigger to update the average rating in FOOD_ESTABLISHMENT when a FOOD_REVIEW is updated
DELIMITER //
CREATE TRIGGER update_average_rating_on_update
AFTER UPDATE ON FOOD_REVIEW
FOR EACH ROW
BEGIN
    DECLARE avg_rating FLOAT;
    SELECT AVG(Rating) INTO avg_rating FROM FOOD_REVIEW WHERE Establishment_id = OLD.Establishment_id;
    UPDATE FOOD_ESTABLISHMENT SET Rating = avg_rating WHERE Establishment_id = OLD.Establishment_id;
END;
//
DELIMITER ;

-- Trigger to update the average rating in FOOD_ESTABLISHMENT when a FOOD_REVIEW is deleted
DELIMITER //
CREATE TRIGGER update_average_rating_on_delete
AFTER DELETE ON FOOD_REVIEW
FOR EACH ROW
BEGIN
    DECLARE avg_rating FLOAT;
    SELECT AVG(Rating) INTO avg_rating FROM FOOD_REVIEW WHERE Establishment_id = OLD.Establishment_id;
    UPDATE FOOD_ESTABLISHMENT SET Rating = avg_rating WHERE Establishment_id = OLD.Establishment_id;
END;
//
DELIMITER ;
reviewsystemdb