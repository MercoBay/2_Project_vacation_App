from flask import jsonify, request
from models.country_model import add_country, get_all_countries, get_country_by_id, update_country, delete_country

# Crear un nuevo país
def create_country(data):
    name = data.get("name")
    if not name:
        return jsonify({"error": "Country name is required"}), 400

    country_id = add_country(name)
    return jsonify({"message": "Country added successfully!", "country_id": country_id}), 201

# Obtener todos los países
def fetch_all_countries():
    countries = get_all_countries()
    return jsonify([{"id": country[0], "name": country[1]} for country in countries]), 200

# Obtener un país por su ID
def get_country_by_id_controller(country_id):
    country = get_country_by_id(country_id)
    if not country:
        return jsonify({"error": "Country not found"}), 404
    return jsonify({"id": country[0], "name": country[1]}), 200

# Actualizar un país
def update_country_controller(country_id, data):
    name = data.get("name")
    if not name:
        return jsonify({"error": "Country name is required"}), 400

    updated = update_country(country_id, name)
    if updated:
        return jsonify({"message": "Country updated successfully!"}), 200
    return jsonify({"error": "Country not found"}), 404

# Eliminar un país
def delete_country_controller(country_id):
    deleted = delete_country(country_id)
    if deleted:
        return jsonify({"message": "Country deleted successfully!"}), 200
    return jsonify({"error": "Country not found"}), 404

