from database import Database

db = Database("mydb")

db.create_table("users")
db.create_table("products")

db.insert("users", {"name": "Divya",   "age": 21, "city": "Chennai"})
db.insert("users", {"name": "Rahul",   "age": 25, "city": "Mumbai"})
db.insert("users", {"name": "Priya",   "age": 21, "city": "Delhi"})
db.insert("users", {"name": "Arjun",   "age": 30, "city": "Chennai"})

db.insert("products", {"name": "Laptop",  "price": 50000, "stock": 10})
db.insert("products", {"name": "Phone",   "price": 20000, "stock": 25})
db.insert("products", {"name": "Tablet",  "price": 30000, "stock": 5})

db.list_tables()

db.select("users")

db.filter("users", age=21)
db.filter("users", city="Chennai")

db.update("users", 2, {"city": "Bangalore"})

db.delete("users", 4)

db.count("users")

db.select("users")

db.select("products")
