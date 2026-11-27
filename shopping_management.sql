-- Online Shopping SQL Project
-- SQLite-compatible setup script

DROP TABLE IF EXISTS products;

CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    price REAL,
    discount INTEGER,
    stock_quantity INTEGER,
    rating REAL,
    brand TEXT,
    description TEXT,
    supplier TEXT
);

INSERT INTO products VALUES
(101, 'Samsung Galaxy Phone', 'Electronics', 25000, 10, 15, 4.5, 'Samsung', 'Smartphone', NULL),
(102, 'Apple iPhone', 'Electronics', 65000, 5, 10, 4.8, 'Apple', 'Premium Mobile', NULL),
(103, 'HP Laptop', 'Electronics', 55000, 15, 8, 4.3, 'HP', 'Business Laptop', NULL),
(104, 'Dell Laptop', 'Electronics', 48000, 10, 12, 4.2, 'Dell', 'Office Laptop', NULL),
(105, 'Nike Shoes', 'Fashion', 3500, 20, 25, 4.4, 'Nike', 'Sports Shoes', NULL),
(106, 'Adidas T Shirt', 'Fashion', 1500, 10, 30, 4.1, 'Adidas', 'Cotton T Shirt', NULL),
(107, 'Puma Bag', 'Fashion', 2500, 15, 18, 4.0, 'Puma', 'Travel Bag', NULL),
(108, 'Wooden Chair', 'Furniture', 4500, 10, 0, 3.9, 'WoodCraft', 'Office Chair', NULL),
(109, 'Office Table', 'Furniture', 8000, 20, 5, 4.2, 'WoodCraft', 'Wooden Table', NULL),
(110, 'Bluetooth Headphones', 'Electronics', 3000, 25, 20, 4.6, 'Boat', 'Wireless Headphones', NULL),
(111, 'Smart Watch', 'Electronics', 5000, 15, 14, 4.3, 'Noise', 'Digital Watch', NULL),
(112, 'Water Bottle', 'Accessories', 500, 5, 50, 3.8, 'Milton', 'Steel Bottle', NULL),
(113, 'School Bag', 'Accessories', 1200, 10, 35, 4.1, 'Skybags', 'Student Bag', NULL),
(114, 'Running Shoes', 'Fashion', 4000, 25, 0, 4.5, 'Nike', 'Running Shoes', NULL),
(115, 'Wireless Mouse', 'Electronics', 900, 10, 40, 4.0, 'Logitech', 'Computer Mouse', NULL);

UPDATE products SET supplier = 'ABC Suppliers' WHERE product_id = 101;
UPDATE products SET supplier = 'XYZ Traders' WHERE product_id = 102;
UPDATE products SET supplier = 'Global Suppliers' WHERE product_id = 103;
