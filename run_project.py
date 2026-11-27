from pathlib import Path
import sqlite3

project_dir = Path(__file__).resolve().parent
database_path = project_dir / "shopping_management.db"

connection = sqlite3.connect(database_path)
connection.row_factory = sqlite3.Row
setup_sql = (project_dir / "shopping_management.sql").read_text(encoding="utf-8")
connection.executescript(setup_sql)

def run(title, sql, limit=15):
    print(f"\n{title}")
    print("-" * 100)
    rows = connection.execute(sql).fetchall()
    if rows:
        print(" | ".join(rows[0].keys()))
        for row in rows[:limit]:
            print(" | ".join("NULL" if value is None else str(value) for value in row))
        if len(rows) > limit:
            print(f"... {len(rows) - limit} more rows")
    print(f"Rows: {len(rows)}")

run("Display All Products", "SELECT * FROM products")
run("Arithmetic - Discounted Price", "SELECT product_name, price, discount, price - (price * discount / 100) AS final_price FROM products")
run("Arithmetic - Price Plus 500", "SELECT product_name, price, price + 500 AS updated_price FROM products")
run("Arithmetic - Stock Value", "SELECT product_name, price, stock_quantity, price * stock_quantity AS stock_value FROM products")
run("Arithmetic - Even Product IDs", "SELECT * FROM products WHERE product_id % 2 = 0")
run("Comparison - Price Above 5000", "SELECT * FROM products WHERE price > 5000")
run("Comparison - Price Below 3000", "SELECT * FROM products WHERE price < 3000")
run("Comparison - 10 Percent Discount", "SELECT * FROM products WHERE discount = 10")
run("Comparison - Rating At Least 4.5", "SELECT * FROM products WHERE rating >= 4.5")
run("Logical AND - Electronics Above 20000", "SELECT * FROM products WHERE category = 'Electronics' AND price > 20000")
run("Logical OR - Fashion or Furniture", "SELECT * FROM products WHERE category = 'Fashion' OR category = 'Furniture'")
run("NOT - Products Not Electronics", "SELECT * FROM products WHERE NOT category = 'Electronics'")
run("BETWEEN - Price 1000 to 5000", "SELECT * FROM products WHERE price BETWEEN 1000 AND 5000")
run("BETWEEN - Discount 10 to 20", "SELECT * FROM products WHERE discount BETWEEN 10 AND 20")
run("IN - Electronics or Fashion", "SELECT * FROM products WHERE category IN ('Electronics', 'Fashion')")
run("NOT IN - Not Furniture or Accessories", "SELECT * FROM products WHERE category NOT IN ('Furniture', 'Accessories')")
run("LIKE - Names Starting with S", "SELECT * FROM products WHERE product_name LIKE 'S%'")
run("LIKE - Names Ending with e", "SELECT * FROM products WHERE product_name LIKE '%e'")
run("LIKE - Names Containing Laptop", "SELECT * FROM products WHERE product_name LIKE '%Laptop%'")
run("NOT LIKE - Names Not Containing Phone", "SELECT * FROM products WHERE product_name NOT LIKE '%Phone%'")
run("Wildcard - Exactly Five Characters", "SELECT * FROM products WHERE product_name LIKE '_____'")
run("Wildcard - S Plus Four Characters", "SELECT * FROM products WHERE product_name LIKE 'S____'")
run("IS NULL - Products Without Supplier", "SELECT * FROM products WHERE supplier IS NULL")
run("IS NOT NULL - Products With Supplier", "SELECT * FROM products WHERE supplier IS NOT NULL")
run("CASE - Price Category", "SELECT product_name, price, CASE WHEN price >= 50000 THEN 'Expensive' WHEN price >= 10000 THEN 'Medium' ELSE 'Affordable' END AS price_category FROM products")
run("CASE - Stock Status", "SELECT product_name, stock_quantity, CASE WHEN stock_quantity = 0 THEN 'Out of Stock' WHEN stock_quantity <= 10 THEN 'Low Stock' ELSE 'Available' END AS stock_status FROM products")
run("CASE - Discount Category", "SELECT product_name, discount, CASE WHEN discount >= 20 THEN 'High Discount' WHEN discount >= 10 THEN 'Medium Discount' ELSE 'Low Discount' END AS discount_status FROM products")
run("Combined - Electronics 10000 to 60000", "SELECT * FROM products WHERE category = 'Electronics' AND price BETWEEN 10000 AND 60000")
run("Combined - Fashion Discount Above 15", "SELECT * FROM products WHERE category = 'Fashion' AND discount > 15")
run("Combined - Nike or Samsung Rating Above 4", "SELECT * FROM products WHERE brand IN ('Nike', 'Samsung') AND rating > 4.0")
run("Combined - Available Below 5000", "SELECT * FROM products WHERE stock_quantity > 0 AND price < 5000")
run("Combined - Expensive or High Discount", "SELECT * FROM products WHERE price > 50000 OR discount >= 20")

print("\nDatabase:", database_path)
connection.close()
