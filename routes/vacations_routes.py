from flask import Blueprint, request
from controllers.vacations_controller import create_vacation_controller, fetch_all_vacations_controller, fetch_vacation_by_id_controller, update_vacation_controller, delete_vacation_controller
from utils.auth import admin_required

vacations_bp = Blueprint("vacations", __name__)

# Route to create a vacation
@vacations_bp.route("/vacations", methods=["POST"])
@admin_required()
def create_vacation():
    data = request.json
    return create_vacation_controller(data)

# Route to get all vacations
@vacations_bp.route("/vacations", methods=["GET"])
def get_all_vacations():
    return fetch_all_vacations_controller()

# Route to get vacation by ID
@vacations_bp.route("/vacations/<int:vacation_id>", methods=["GET"])
def get_vacation_by_id(vacation_id):
    return fetch_vacation_by_id_controller(vacation_id)

# Route to update a vacation
@vacations_bp.route("/vacations/<int:vacation_id>", methods=["PUT"])
@admin_required()
def update_vacation(vacation_id):
    data = request.json
    return update_vacation_controller(vacation_id, data)

# Route to delete a vacation
@vacations_bp.route("/vacations/<int:vacation_id>", methods=["DELETE"])
@admin_required()
def delete_vacation(vacation_id):
    return delete_vacation_controller(vacation_id)

# from flask import Blueprint, request
# from controllers.vacations_controller import create_vacation_controller, fetch_all_vacations_controller, fetch_vacation_by_id_controller, update_vacation_controller, delete_vacation_controller

# vacations_bp = Blueprint("vacations", __name__)

# # Route to create a vacation
# @vacations_bp.route("/vacations", methods=["POST"])
# def create_vacation():
#     data = request.json
#     return create_vacation_controller(data)

# # Route to get all vacations
# @vacations_bp.route("/vacations", methods=["GET"])
# def get_all_vacations():
#     return fetch_all_vacations_controller()

# # Route to get vacation by ID
# @vacations_bp.route("/vacations/<int:vacation_id>", methods=["GET"])
# def get_vacation_by_id(vacation_id):
#     return fetch_vacation_by_id_controller(vacation_id)

# # Route to update a vacation
# @vacations_bp.route("/vacations/<int:vacation_id>", methods=["PUT"])
# def update_vacation(vacation_id):
#     data = request.json
#     return update_vacation_controller(vacation_id, data)

# # Route to delete a vacation
# @vacations_bp.route("/vacations/<int:vacation_id>", methods=["DELETE"])
# def delete_vacation(vacation_id):
#     return delete_vacation_controller(vacation_id)

