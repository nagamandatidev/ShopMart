# create_tables.py
from database import engine
import models

print("🔄 Creating tables...")

# This will create tables if they don't exist already
models.Base.metadata.create_all(bind=engine)

print("✅ Tables created successfully!")
