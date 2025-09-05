# backend/create_tables.py
from backend.database import engine   # 🔹 absolute import
from backend import models            # 🔹 absolute import

print("🔄 Creating tables...")

models.Base.metadata.create_all(bind=engine)

print("✅ Tables created successfully!")
