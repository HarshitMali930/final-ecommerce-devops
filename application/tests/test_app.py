import sys
import os

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "app")
    )
)

from app import app


def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200


def test_products():
    client = app.test_client()
    response = client.get("/products")
    assert response.status_code == 200


def test_recommendations_by_category_and_price():
    client = app.test_client()
    response = client.get("/recommendations?category=Electronics&max_price=30000")

    assert response.status_code == 200
    data = response.get_json()
    assert data["method"] == "content-based filtering"
    assert data["count"] == len(data["recommendations"])
    assert all(
        product["category"].lower() == "electronics"
        and product["price"] <= 30000
        for product in data["recommendations"]
    )


def test_recommendations_rejects_invalid_max_price():
    client = app.test_client()
    response = client.get("/recommendations?max_price=abc")

    assert response.status_code == 400
    assert response.get_json()["error"] == "max_price must be a non-negative number"


def test_recommendations_rejects_negative_max_price():
    client = app.test_client()
    response = client.get("/recommendations?max_price=-100")

    assert response.status_code == 400
    assert response.get_json()["error"] == "max_price must be a non-negative number"
