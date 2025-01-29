from flask import Blueprint, request
from controllers.roles_controller import (
    create_role,
    fetch_all_roles,
    fetch_role_by_id,
    update_role_controller,
    delete_role_controller
)

roles_bp = Blueprint("roles_routes", __name__)

# Route to add a role
@roles_bp.route("/roles", methods=["POST"])
def add_role_route():
    return create_role(request.json)

# Route to get all roles
@roles_bp.route("/roles", methods=["GET"])
def get_all_roles_route():
    return fetch_all_roles()

# Route to get a role by ID
@roles_bp.route("/roles/<int:role_id>", methods=["GET"])
def get_role_by_id_route(role_id):
    return fetch_role_by_id(role_id)

# Route to update a role
@roles_bp.route("/roles/<int:role_id>", methods=["PUT"])
def update_role_route(role_id):
    return update_role_controller(role_id, request.json)

# Route to delete a role
@roles_bp.route("/roles/<int:role_id>", methods=["DELETE"])
def delete_role_route(role_id):
    return delete_role_controller(role_id)
