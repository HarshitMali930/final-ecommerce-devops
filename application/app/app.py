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
    return jsonify({"status": "healthy"})


@app.route("/products")
def get_products():
    app.logger.info("Products endpoint accessed")
    return jsonify(products)



@app.route("/recommendations")
def recommendations():
    from flask import request

    category = request.args.get("category", "").strip().lower()
    raw_max_price = request.args.get("max_price")
    try:
        max_price = float(raw_max_price) if raw_max_price else None
        if max_price is not None and max_price < 0:
            raise ValueError
    except ValueError:
        return jsonify({"error": "max_price must be a non-negative number"}), 400

    results = [
        product for product in products
        if (not category or product["category"].lower() == category)
        and (max_price is None or product["price"] <= max_price)
    ]

    app.logger.info(
        "Product recommendations requested: category=%s max_price=%s results=%d",
        category or "all", max_price, len(results)
    )

    return jsonify({
        "recommendations": results,
        "count": len(results),
        "method": "content-based filtering"
    })

@app.route("/metrics")
def metrics():
    return "ecommerce_app_up 1\n", 200, {
        "Content-Type": "text/plain; version=0.0.4"
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
