from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Health check endpoint for liveness probe
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

# Health check endpoint for readiness probe
@app.route('/ready', methods=['GET'])
def ready_check():
    return jsonify({"status": "ready"}), 200

# Simulated in-memory inventory storage
inventories = {}

@app.route('/inventory', methods=['POST'])
def add_inventory():
    data = request.get_json()
    product_id = data['product_id']
    quantity = data['quantity']
    inventories[product_id] = quantity
    return jsonify({"message": "Inventory added"}), 201

@app.route('/inventory', methods=['PUT'])
def update_inventory():
    data = request.get_json()
    product_id = data['product_id']
    if product_id in inventories:
        inventories[product_id] = data['quantity']
        return jsonify({"message": "Inventory updated"}), 200
    return jsonify({"message": "Product not found"}), 404

@app.route('/inventory', methods=['GET'])
def get_inventory():
    return jsonify(inventories)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)

