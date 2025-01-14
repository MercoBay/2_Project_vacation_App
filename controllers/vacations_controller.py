from flask import jsonify, request
from models.vacations_model import add_vacation, get_all_vacations, get_vacation_by_id, update_vacation, delete_vacation

# Create vacation
def create_vacation_controller(data):
    country_id = data.get("country_id")
    description = data.get("description")
    start_date = data.get("start_date")
    end_date = data.get("end_date")
    price = data.get("price")
    image_url = data.get("image_url")
    
    if not country_id or not description or not start_date or not end_date or not price:
        return jsonify({"error": "Missing required fields"}), 400

    vacation_id = add_vacation(country_id, description, start_date, end_date, price, image_url)
    if vacation_id:
        return jsonify({"message": "Vacation added successfully!", "vacation_id": vacation_id}), 201
    return jsonify({"error": "Failed to add vacation"}), 500

# Get all vacations
def fetch_all_vacations_controller():
    vacations = get_all_vacations()
    vacation_list = [{"id": v[0], "country_id": v[1], "description": v[2], "start_date": v[3], "end_date": v[4], "price": v[5], "image_url": v[6]} for v in vacations]
    return jsonify(vacation_list), 200

# Get vacation by ID
def fetch_vacation_by_id_controller(vacation_id):
    vacation = get_vacation_by_id(vacation_id)
    if vacation:
        vacation_data = {"id": vacation[0], "country_id": vacation[1], "description": vacation[2], "start_date": vacation[3], "end_date": vacation[4], "price": vacation[5], "image_url": vacation[6]}
        return jsonify(vacation_data), 200
    return jsonify({"error": "Vacation not found"}), 404

# Update vacation
def update_vacation_controller(vacation_id, data):
    updated = update_vacation(vacation_id, data.get("country_id"), data.get("description"), data.get("start_date"), data.get("end_date"), data.get("price"), data.get("image_url"))
    if updated:
        return jsonify({"message": "Vacation updated successfully!"}), 200
    return jsonify({"error": "Vacation not found"}), 404

# Delete vacation
def delete_vacation_controller(vacation_id):
    deleted = delete_vacation(vacation_id)
    if deleted:
        return jsonify({"message": "Vacation deleted successfully!"}), 200
    return jsonify({"error": "Vacation not found"}), 404
