from database import SessionLocal, engine
import models

# Make sure tables exist
models.Base.metadata.create_all(bind=engine)

db = SessionLocal()

sample_products = [
    {"name": "iPhone 15", "description": "Latest Apple smartphone", "price": 999.99, "image": "https://via.placeholder.com/150"},
    {"name": "Samsung TV", "description": "55 inch 4K UHD Smart TV", "price": 599.99, "image": "https://via.placeholder.com/150"},
    {"name": "Nike Running Shoes", "description": "Comfortable and lightweight shoes", "price": 120.00, "image": "https://via.placeholder.com/150"},
    {"name": "Milk", "description": "1 Gallon organic whole milk", "price": 4.50, "image": "https://via.placeholder.com/150"},
    {"name": "Laptop", "description": "Powerful laptop with 16GB RAM", "price": 1299.99, "image": "https://via.placeholder.com/150"},
]

for p in sample_products:
    prod = models.Product(**p)
    db.add(prod)

db.commit()
db.close()

print("✅ Sample products inserted!")
