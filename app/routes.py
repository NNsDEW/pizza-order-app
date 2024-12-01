# app/routes.py
from flask import Blueprint, request, jsonify

bp = Blueprint('main', __name__)

# Пример меню
menu = [
    {"id": 1, "name": "Margherita", "price": 10},
    {"id": 2, "name": "Pepperoni", "price": 12},
    {"id": 3, "name": "Vegetarian", "price": 11}
]

# Маршрут для получения меню
@bp.route('/menu', methods=['GET'])
def get_menu():
    return jsonify(menu)

# Маршрут для размещения заказа
@bp.route('/orders', methods=['POST'])
def place_order():
    order_data = request.json
    if not order_data or 'items' not in order_data:
        return jsonify({"error": "Invalid order data"}), 400

    # Логика размещения заказа
    return jsonify({"message": "Order placed successfully!"}), 201
