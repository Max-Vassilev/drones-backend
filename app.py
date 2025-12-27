from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_migrate import Migrate
import redis, json, time

from models import db, Product, CustomerOrder, CustomerOrderItem

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://drones_user:drones_password@drones-postgres-db:5432/drones_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)

# Create Redis client connection to Redis service
redis_client = redis.Redis(host="drones-redis", port=6379, db=0, decode_responses=True)

@app.route("/products", methods=["GET"])
def get_products():
    start_time = time.time()

    # Try to get cached products list from Redis
    cached_products = redis_client.get("all_products")

    if cached_products:
        print(f"[REDIS] Cache HIT | {time.time() - start_time:.4f}s", flush=True)
        return jsonify(json.loads(cached_products))

    print("[REDIS] Cache MISS", flush=True)

    products_list = [{
        "id": p.id,
        "name": p.name,
        "type": p.type,
        "price": p.price,
        "description": p.description,
        "image": p.image
    } for p in Product.query.all()]

    # Store products list in Redis with 5-minute expiration
    redis_client.setex("all_products", 300, json.dumps(products_list))
    print(f"[REDIS] Cache SET | {time.time() - start_time:.4f}s", flush=True)

    return jsonify(products_list)

@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    p = Product.query.get_or_404(product_id)
    return jsonify({
        "id": p.id,
        "name": p.name,
        "type": p.type,
        "price": p.price,
        "description": p.description,
        "full_description": p.full_description,
        "image": p.image
    })

@app.route("/orders", methods=["POST"])
def create_order():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    order = CustomerOrder(
        first_name=data["first_name"], last_name=data["last_name"],
        phone=data["phone"], courier=data["courier"], address=data["address"]
    )

    db.session.add(order)
    db.session.flush()

    for i in data["items"]:
        db.session.add(CustomerOrderItem(order_id=order.id, product_id=i["product_id"], quantity=i["quantity"]))

    db.session.commit()

    # Remove cached products so next request gets fresh data
    redis_client.delete("all_products")
    print("[REDIS] Cache INVALIDATED", flush=True)

    return jsonify({"order_id": order.id}), 201

@app.route("/about", methods=["GET"])
def about_page():
    return jsonify({"title": "About This Project", "description": "Flask + React + PostgreSQL + Docker"})

@app.route("/contacts", methods=["GET"])
def contacts_page():
    return jsonify({"name": "Maxim Vassilev", "title": "Full Stack Web Developer & DevOps Engineer", "location": "Sofia, Bulgaria"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=False, use_reloader=False)
