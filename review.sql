CREATE DATABASE IF NOT EXISTS FoodReviewDB;
USE FoodReviewDB;

-- Table for ADMIN
CREATE TABLE ADMIN (
    admin_id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL
);

-- Table for CUSTOMER
CREATE TABLE CUSTOMER (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    middle_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    birthday DATE NOT NULL,
    age INT NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Table for FOOD_ESTABLISHMENT
CREATE TABLE FOOD_ESTABLISHMENT (
    establishment_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    baranggay VARCHAR(100) NOT NULL,
    postal_code VARCHAR(25) NOT NULL,
    street VARCHAR(100) NOT NULL,
    city VARCHAR(100) NOT NULL,
    province VARCHAR(100) NOT NULL,
    rating DECIMAL(2,1) DEFAULT 0, -- Initial value set to 0
    average_price DECIMAL(6,2) DEFAULT 0, -- Initial value set to 0
    food_type_served VARCHAR(100) NOT NULL
);

-- Table for FOOD_ITEM
CREATE TABLE FOOD_ITEM (
    food_id INT AUTO_INCREMENT PRIMARY KEY,
    price DECIMAL(6,2) NOT NULL,
    rating DECIMAL(2,1) NOT NULL DEFAULT 0, -- Initial value set to 0
    name VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    establishment_id INT,
    FOREIGN KEY (establishment_id) REFERENCES FOOD_ESTABLISHMENT(establishment_id)
);

-- Table for FOOD_REVIEW
CREATE TABLE FOOD_REVIEW (
    review_id INT AUTO_INCREMENT PRIMARY KEY,
    review_date DATE NOT NULL,
    review_time TIME NOT NULL,
    type_of_review VARCHAR(50) NOT NULL,
    rating DECIMAL(2,1) NOT NULL DEFAULT 0,
    title VARCHAR(255) NOT NULL,
    suggestion TEXT NOT NULL,
    customer_id INT,
    establishment_id INT,
    food_id INT,
    FOREIGN KEY (customer_id) REFERENCES CUSTOMER(customer_id),
    FOREIGN KEY (establishment_id) REFERENCES FOOD_ESTABLISHMENT(establishment_id),
    FOREIGN KEY (food_id) REFERENCES FOOD_ITEM(food_id)
);

-- Table for FOOD_ITEM_INGREDIENT
CREATE TABLE FOOD_ITEM_INGREDIENT (
    food_id INT,
    ingredient VARCHAR(100),
    FOREIGN KEY (food_id) REFERENCES FOOD_ITEM(food_id),
    PRIMARY KEY (food_id, ingredient)
);

-- Table for MEAT
CREATE TABLE MEAT (
    food_id INT,
    meat_type VARCHAR(100),
    FOREIGN KEY (food_id) REFERENCES FOOD_ITEM(food_id),
    PRIMARY KEY (food_id, meat_type)
);

-- Table for VEGETABLE
CREATE TABLE VEGETABLE (
    food_id INT,
    vegetable_type VARCHAR(100),
    FOREIGN KEY (food_id) REFERENCES FOOD_ITEM(food_id),
    PRIMARY KEY (food_id, vegetable_type)
);

-- Table for DESSERT
CREATE TABLE DESSERT (
    food_id INT,
    dessert_type VARCHAR(100),
    FOREIGN KEY (food_id) REFERENCES FOOD_ITEM(food_id),
    PRIMARY KEY (food_id, dessert_type)
);

-- -- Trigger to update the average price in FOOD_ESTABLISHMENT when a FOOD_ITEM is inserted
-- DELIMITER //
-- CREATE TRIGGER ESTABLISHMENT_update_average_price
-- AFTER INSERT ON FOOD_ITEM
-- FOR EACH ROW
-- BEGIN
--     DECLARE avg_price DECIMAL(6,2);
--     SELECT AVG(price) INTO avg_price FROM FOOD_ITEM WHERE establishment_id = NEW.establishment_id;
--     UPDATE FOOD_ESTABLISHMENT SET average_price = avg_price WHERE establishment_id = NEW.establishment_id;
-- END;
-- //
-- DELIMITER ;

-- -- Trigger to update the average price in FOOD_ESTABLISHMENT when a FOOD_ITEM is updated
-- DELIMITER //
-- CREATE TRIGGER ESTABLISHMENT_update_average_price_on_update
-- AFTER UPDATE ON FOOD_ITEM
-- FOR EACH ROW
-- BEGIN
--     DECLARE avg_price DECIMAL(6,2);
--     SELECT AVG(price) INTO avg_price FROM FOOD_ITEM WHERE establishment_id = OLD.establishment_id;
--     UPDATE FOOD_ESTABLISHMENT SET average_price = avg_price WHERE establishment_id = OLD.establishment_id;
-- END;
-- //
-- DELIMITER ;

-- -- Trigger to update the average rating in FOOD_ESTABLISHMENT when a FOOD_REVIEW is inserted
-- DELIMITER //
-- CREATE TRIGGER ESTABLISHMENT_update_average_rating
-- AFTER INSERT ON FOOD_REVIEW
-- FOR EACH ROW
-- BEGIN
--     DECLARE avg_rating DECIMAL(2,1);
--     IF NEW.establishment_id IS NOT NULL AND NEW.food_id IS NULL THEN
--         SELECT AVG(rating) INTO avg_rating FROM FOOD_REVIEW WHERE establishment_id = NEW.establishment_id;
--         UPDATE FOOD_ESTABLISHMENT SET rating = avg_rating WHERE establishment_id = NEW.establishment_id;
--     END IF;
-- END;
-- //
-- DELIMITER ;

-- -- Trigger to update the average rating in FOOD_ESTABLISHMENT when a FOOD_REVIEW is updated
-- DELIMITER //
-- CREATE TRIGGER ESTABLISHMENT_update_average_rating_on_update
-- AFTER UPDATE ON FOOD_REVIEW
-- FOR EACH ROW
-- BEGIN
--     DECLARE avg_rating DECIMAL(2,1);
--     IF OLD.establishment_id IS NOT NULL AND OLD.food_id IS NULL THEN
--         SELECT AVG(rating) INTO avg_rating FROM FOOD_REVIEW WHERE establishment_id = OLD.establishment_id;
--         UPDATE FOOD_ESTABLISHMENT SET rating = avg_rating WHERE establishment_id = OLD.establishment_id;
--     END IF;
-- END;
-- //
-- DELIMITER ;

-- -- Trigger to update the average rating in FOOD_ESTABLISHMENT when a FOOD_REVIEW is deleted
-- DELIMITER //
-- CREATE TRIGGER ESTABLISHMENT_update_average_rating_on_delete
-- AFTER DELETE ON FOOD_REVIEW
-- FOR EACH ROW
-- BEGIN
--     DECLARE avg_rating DECIMAL(2,1);
--     IF OLD.establishment_id IS NOT NULL AND OLD.food_id IS NULL THEN
--         SELECT AVG(rating) INTO avg_rating FROM FOOD_REVIEW WHERE establishment_id = OLD.establishment_id;

--         IF avg_rating IS NULL THEN
--             SET avg_rating = 0.0; -- Set a default value if there are no reviews
--         END IF;

--         UPDATE FOOD_ESTABLISHMENT SET rating = avg_rating WHERE establishment_id = OLD.establishment_id;
--     END IF;
-- END;
-- //
-- DELIMITER ;

-- -- Trigger to update the average rating in FOOD_ITEM when a FOOD_REVIEW is inserted
-- DELIMITER //
-- CREATE TRIGGER ITEM_update_food_item_rating
-- AFTER INSERT ON FOOD_REVIEW
-- FOR EACH ROW
-- BEGIN
--     DECLARE avg_rating DECIMAL(2,1);
--     IF NEW.food_id IS NOT NULL THEN
--         SELECT AVG(rating) INTO avg_rating FROM FOOD_REVIEW WHERE food_id = NEW.food_id;
--         UPDATE FOOD_ITEM SET rating = avg_rating WHERE food_id = NEW.food_id;
--     END IF;
-- END;
-- //
-- DELIMITER ;

-- -- Trigger to update the average rating in FOOD_ITEM when a FOOD_REVIEW is updated
-- DELIMITER //
-- CREATE TRIGGER ITEM_update_food_item_rating_on_update
-- AFTER UPDATE ON FOOD_REVIEW
-- FOR EACH ROW
-- BEGIN
--     DECLARE avg_rating DECIMAL(2,1);
--     IF OLD.food_id IS NOT NULL THEN
--         SELECT AVG(rating) INTO avg_rating FROM FOOD_REVIEW WHERE food_id = OLD.food_id;
--         UPDATE FOOD_ITEM SET rating = avg_rating WHERE food_id = OLD.food_id;
--     END IF;
-- END;
-- //
-- DELIMITER ;

-- DELIMITER //
-- CREATE TRIGGER ITEM_update_food_item_rating_on_delete
-- AFTER DELETE ON FOOD_REVIEW
-- FOR EACH ROW
-- BEGIN
--     DECLARE avg_rating DECIMAL(2,1);
    
--     IF OLD.food_id IS NOT NULL THEN
--         SELECT AVG(rating) INTO avg_rating FROM FOOD_REVIEW WHERE food_id = OLD.food_id;
        
--         IF avg_rating IS NULL THEN
--             SET avg_rating = 0.0; -- Set a default value if there are no reviews
--         END IF;
        
--         UPDATE FOOD_ITEM SET rating = avg_rating WHERE food_id = OLD.food_id;
--     END IF;
-- END;
-- //
-- DELIMITER ;
