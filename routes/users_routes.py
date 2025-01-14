from flask import Blueprint, request
from controllers.users_controller import (
    create_user_controller,
    fetch_all_users_controller,
    fetch_user_by_id_controller,
    update_user_controller,
    delete_user_controller
)

# Cambia el nombre del Blueprint a `users_bp` en lugar de `user_bp`
users_bp = Blueprint('users_routes', __name__)

# Rutas de usuarios
@users_bp.route('/users', methods=['POST'])
def create_user():
    return create_user_controller(request.json)

@users_bp.route('/users', methods=['GET'])
def get_all_users():
    return fetch_all_users_controller()

@users_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
    return fetch_user_by_id_controller(user_id)

@users_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    return update_user_controller(user_id, request.json)

@users_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return delete_user_controller(user_id)
