
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from . import models, database, auth, schemas

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Walmart Clone API")

origins = ["http://localhost:5173"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/products")
def get_products(db: Session = Depends(database.get_db)):
    return db.query(models.Product).all()

@app.get("/products/{product_id}")
def get_product(product_id: int, db: Session = Depends(database.get_db)):
    prod = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not prod:
        raise HTTPException(status_code=404, detail="Product not found")
    return prod

@app.post("/auth/register")
def register(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    return auth.create_user(db, user)

@app.post("/auth/login")
def login(data: schemas.LoginRequest, db: Session = Depends(database.get_db)):
    return auth.login_user(db, data)
