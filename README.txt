Project Description:

This project manages an online shopping platform where customers can purchase products. It stores product details, prices, discounts, stock quantities, and product categories.
We'll use SQL operators to filter products, calculate prices, identify discounts, and manage product availability.

1.Create Database

CREATE DATABASE shopping_management;

USE shopping_management;

2: Create Products Table

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10,2),
    discount INT,
    stock_quantity INT,
    rating DECIMAL(2,1),
    brand VARCHAR(50),
    description VARCHAR(150)
);

3: Insert Sample Data
Insert 15 sample products.

INSERT INTO products VALUES
(101, 'Samsung Galaxy Phone', 'Electronics', 25000, 10, 15, 4.5, 'Samsung', 'Smartphone'),
(102, 'Apple iPhone', 'Electronics', 65000, 5, 10, 4.8, 'Apple', 'Premium Mobile'),
(103, 'HP Laptop', 'Electronics', 55000, 15, 8, 4.3, 'HP', 'Business Laptop'),
(104, 'Dell Laptop', 'Electronics', 48000, 10, 12, 4.2, 'Dell', 'Office Laptop'),
(105, 'Nike Shoes', 'Fashion', 3500, 20, 25, 4.4, 'Nike', 'Sports Shoes'),
(106, 'Adidas T Shirt', 'Fashion', 1500, 10, 30, 4.1, 'Adidas', 'Cotton T Shirt'),
(107, 'Puma Bag', 'Fashion', 2500, 15, 18, 4.0, 'Puma', 'Travel Bag'),
(108, 'Wooden Chair', 'Furniture', 4500, 10, 0, 3.9, 'WoodCraft', 'Office Chair'),
(109, 'Office Table', 'Furniture', 8000, 20, 5, 4.2, 'WoodCraft', 'Wooden Table'),
(110, 'Bluetooth Headphones', 'Electronics', 3000, 25, 20, 4.6, 'Boat', 'Wireless Headphones'),
(111, 'Smart Watch', 'Electronics', 5000, 15, 14, 4.3, 'Noise', 'Digital Watch'),
(112, 'Water Bottle', 'Accessories', 500, 5, 50, 3.8, 'Milton', 'Steel Bottle'),
(113, 'School Bag', 'Accessories', 1200, 10, 35, 4.1, 'Skybags', 'Student Bag'),
(114, 'Running Shoes', 'Fashion', 4000, 25, 0, 4.5, 'Nike', 'Running Shoes'),
(115, 'Wireless Mouse', 'Electronics', 900, 10, 40, 4.0, 'Logitech', 'Computer Mouse');

4: SELECT – Display All Products

SELECT * FROM products;

5: Arithmetic Operators

Arithmetic operators perform mathematical calculations.

Operators: +, -, *, /, %

Calculate discounted price

SELECT
    product_name,
    price,
    discount,
    price - (price * discount / 100) AS final_price
FROM products;

Increase product price by ₹500

SELECT
    product_name,
    price,
    price + 500 AS updated_price
FROM products;

Calculate total stock value

SELECT
    product_name,
    price,
    stock_quantity,
    price * stock_quantity AS stock_value
FROM products;

Find products with even product IDs

SELECT *
FROM products
WHERE product_id % 2 = 0;

6: Comparison Operators

Comparison operators compare two values.

Operators: =, !=, <>, >, <, >=, <=

Products costing more than ₹5,000

SELECT *
FROM products
WHERE price > 5000;

Products costing less than ₹3,000

SELECT *
FROM products
WHERE price < 3000;

Products with a 10% discount

SELECT *
FROM products
WHERE discount = 10;

Products with a rating of at least 4.5

SELECT *
FROM products
WHERE rating >= 4.5;

7: Logical Operators (AND, OR, NOT)

AND – Both conditions must be true.
Find Electronics products costing more than ₹20,000.

SELECT *
FROM products
WHERE category = 'Electronics'
AND price > 20000;

OR – At least one condition must be true.
Find products belonging to Fashion or Furniture.

SELECT *
FROM products
WHERE category = 'Fashion'
OR category = 'Furniture';

NOT – Reverse the condition.
Display products that are not Electronics.

SELECT *
FROM products
WHERE NOT category = 'Electronics';

8: BETWEEN
Find products priced between ₹1,000 and ₹5,000.

SELECT *
FROM products
WHERE price BETWEEN 1000 AND 5000;

        Find products with discounts between 10% and 20%.

SELECT *
FROM products
WHERE discount BETWEEN 10 AND 20;

9: IN and NOT IN
IN
Find products from selected categories.

SELECT *
FROM products
WHERE category IN ('Electronics', 'Fashion');

NOT IN
Exclude selected categories.

SELECT *
FROM products
WHERE category NOT IN ('Furniture', 'Accessories');

10: LIKE and NOT LIKE
LIKE searches for matching text patterns.

1.Product names starting with S

SELECT *
FROM products
WHERE product_name LIKE 'S%';

2. Product names ending with e

SELECT *
FROM products
WHERE product_name LIKE '%e';

3. Product names containing Laptop

SELECT *
FROM products
WHERE product_name LIKE '%Laptop%';

4. Products not containing Phone

SELECT *
FROM products
WHERE product_name NOT LIKE '%Phone%';

11: Wildcards (% and _)
% – Represents zero or more characters.

SELECT *
FROM products
WHERE product_name LIKE '%Shoes%';
    
         _ – Represents exactly one character.

         Find product names with five characters.

SELECT *
FROM products
WHERE product_name LIKE '_____';

          Find product names starting with S followed by any four characters.

SELECT *
FROM products
WHERE product_name LIKE 'S____';

12: IS NULL and IS NOT NULL
First, let's add a supplier column.

ALTER TABLE products
ADD supplier VARCHAR(100);

          Insert supplier details for selected products.

UPDATE products
SET supplier = 'ABC Suppliers'
WHERE product_id = 101;

UPDATE products
SET supplier = 'XYZ Traders'
WHERE product_id = 102;

UPDATE products
SET supplier = 'Global Suppliers'
WHERE product_id = 103;

	Find products without supplier details.

SELECT *
FROM products
WHERE supplier IS NULL;

	Find products with supplier details.

SELECT *
FROM products
WHERE supplier IS NOT NULL;

STEP 13: CASE WHEN
CASE WHEN is used to create conditional results.

1. Product price category

SELECT
    product_name,
    price,
    CASE
        WHEN price >= 50000 THEN 'Expensive'
        WHEN price >= 10000 THEN 'Medium'
        ELSE 'Affordable'
    END AS price_category
FROM products;

2. Stock availability

SELECT
    product_name,
    stock_quantity,
    CASE
        WHEN stock_quantity = 0 THEN 'Out of Stock'
        WHEN stock_quantity <= 10 THEN 'Low Stock'
        ELSE 'Available'
    END AS stock_status
FROM products;

3. Discount category

SELECT
    product_name,
    discount,
    CASE
        WHEN discount >= 20 THEN 'High Discount'
        WHEN discount >= 10 THEN 'Medium Discount'
        ELSE 'Low Discount'
    END AS discount_status
FROM products;

14: Combining Multiple Conditions
This is where we combine multiple SQL concepts.

1. Electronics products between ₹10,000 and ₹60,000.

SELECT *
FROM products
WHERE category = 'Electronics'
AND price BETWEEN 10000 AND 60000;

2. Fashion products with a discount above 15%.

SELECT *
FROM products
WHERE category = 'Fashion'
AND discount > 15;

3. Products from Nike or Samsung with a rating above 4.0.

SELECT *
FROM products
WHERE brand IN ('Nike', 'Samsung')
AND rating > 4.0;

4. Available products costing less than ₹5,000.

SELECT *
FROM products
WHERE stock_quantity > 0
AND price < 5000;

5. Find products that are either expensive or have high discounts.

SELECT *
FROM products
WHERE price > 50000
OR discount >= 20;
