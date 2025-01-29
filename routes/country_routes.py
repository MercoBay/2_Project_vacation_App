from flask import Blueprint, request
from controllers.country_controller import (
    create_country,
    fetch_all_countries,
    get_country_by_id_controller,
    update_country_controller,
    delete_country_controller
)

country_bp = Blueprint("country_routes", __name__)

# Ruta para añadir un país
@country_bp.route("/countries", methods=["POST"])
def add_country_route():
    return create_country(request.json)

# Ruta para obtener todos los países
@country_bp.route("/countries", methods=["GET"])
def get_all_countries_route():
    return fetch_all_countries()

# Ruta para obtener un país por ID
@country_bp.route("/countries/<int:country_id>", methods=["GET"])
def get_country_by_id_route(country_id):
    return get_country_by_id_controller(country_id)

# Ruta para actualizar un país
@country_bp.route("/countries/<int:country_id>", methods=["PUT"])
def update_country_route(country_id):
    return update_country_controller(country_id, request.json)

# Ruta para eliminar un país
@country_bp.route("/countries/<int:country_id>", methods=["DELETE"])
def delete_country_route(country_id):
    return delete_country_controller(country_id)
