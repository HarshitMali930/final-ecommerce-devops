from flask import Flask, jsonify
import logging

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 55000,
        "category": "Electronics"
    },
    {
        "id": 2,
        "name": "Smartphone",
        "price": 25000,
        "category": "Electronics"
    },
    {
        "id": 3,
        "name": "Headphones",
        "price": 2500,
        "category": "Accessories"
    }
]


@app.route("/")
def home():
    app.logger.info("Home endpoint accessed")
    return jsonify({
        "message": "AI-Powered E-Commerce Platform",
        "status": "running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/products")
def get_products():
    app.logger.info("Products endpoint accessed")
    return jsonify(products)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
