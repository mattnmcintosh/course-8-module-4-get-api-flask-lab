from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Welcome to the Product API!", "resource_endpoints": "/products, /products?category=<category>, /products/<id>"}), 200

@app.route("/products", methods=["GET"])
def get_products():
    category = request.args.get("category")
    if category:
        filtered = [item for item in products if item["category"] == category]
        return jsonify(filtered), 200
    return jsonify(products), 200

@app.route("/products/<int:id>", methods=["GET"])
def get_product_by_id(id):
    for p in products:
       if p["id"] == id:
          return jsonify(p), 200
    return jsonify({"message": "Product not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
