from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from typing import List

DATABASE_URL = "postgresql://drones_user:drones_password@drones-postgres:5432/drones_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()


class OrderItem(BaseModel):
    product_id: int
    quantity: int


class OrderCreate(BaseModel):
    first_name: str
    last_name: str
    phone: str
    courier: str
    address: str
    items: List[OrderItem]


@app.get("/products")
def get_products():
    with engine.connect() as conn:
        result = conn.execute(text("""
            SELECT id, name, type, price, description, image
            FROM products
        """))
        return [dict(row._mapping) for row in result]


@app.get("/products/{product_id}")
def get_product(product_id: int):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM products WHERE id = :id"),
            {"id": product_id}
        ).fetchone()

        if not result:
            raise HTTPException(status_code=404, detail="Product not found")

        return dict(result._mapping)


@app.post("/orders")
def create_order(order: OrderCreate):
    with engine.begin() as conn:
        order_result = conn.execute(text("""
            INSERT INTO customer_orders
            (first_name, last_name, phone, courier, address)
            VALUES (:first_name, :last_name, :phone, :courier, :address)
            RETURNING id
        """), order.dict())

        order_id = order_result.fetchone()[0]

        for item in order.items:
            conn.execute(text("""
                INSERT INTO customer_order_items
                (order_id, product_id, quantity)
                VALUES (:order_id, :product_id, :quantity)
            """), {
                "order_id": order_id,
                "product_id": item.product_id,
                "quantity": item.quantity
            })

    return {"order_id": order_id}


@app.get("/about")
def about_page():
    return {
        "title": "About This Project",
        "description": "FastAPI + React + PostgreSQL + Docker"
    }


@app.get("/contacts")
def contacts_page():
    return {
        "name": "Maxim Vassilev",
        "title": "Full Stack Web Developer & DevOps Engineer",
        "location": "Sofia, Bulgaria"
    }
