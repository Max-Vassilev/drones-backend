from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_migrate import Migrate
import redis
import json

from models import db, Product, CustomerOrder, CustomerOrderItem

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://drones_user:drones_password@postgres_db-container:5432/drones_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)

redis_client = redis.Redis(
    host="redis-container",
    port=6379,
    db=0,
    decode_responses=True
)

@app.route("/products", methods=["GET"])
def get_products():
    cached_products = redis_client.get("all_products")

    if cached_products:
        print("[REDIS] Cache HIT", flush=True)
        return jsonify(json.loads(cached_products))

    print("[REDIS] Cache MISS", flush=True)

    products = Product.query.all()
    products_list = [
        {
            "id": p.id,
            "name": p.name,
            "type": p.type,
            "price": p.price,
            "description": p.description,
            "image": p.image
        } for p in products
    ]

    redis_client.setex("all_products", 300, json.dumps(products_list))
    print("[REDIS] Cache SET", flush=True)

    return jsonify(products_list)

@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = Product.query.get_or_404(product_id)
    return jsonify({
        "id": product.id,
        "name": product.name,
        "type": product.type,
        "price": product.price,
        "description": product.description,
        "full_description": product.full_description,
        "image": product.image
    })

@app.route("/about", methods=["GET"])
def about_page():
    return jsonify({
        "title": "About This Project",
        "description": "Flask + React + PostgreSQL + Docker"
    })

@app.route("/contacts", methods=["GET"])
def contacts_page():
    return jsonify({
        "name": "Maxim Vassilev",
        "title": "Full Stack Web Developer & DevOps Engineer",
        "location": "Sofia, Bulgaria"
    })

@app.route("/orders", methods=["POST"])
def create_order():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    order = CustomerOrder(
        first_name=data["first_name"],
        last_name=data["last_name"],
        phone=data["phone"],
        courier=data["courier"],
        address=data["address"]
    )

    db.session.add(order)
    db.session.flush()

    for item in data["items"]:
        db.session.add(CustomerOrderItem(
            order_id=order.id,
            product_id=item["product_id"],
            quantity=item["quantity"]
        ))

    db.session.commit()

    redis_client.delete("all_products")
    print("[REDIS] Cache INVALIDATED", flush=True)

    return jsonify({"order_id": order.id}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False, use_reloader=False)
