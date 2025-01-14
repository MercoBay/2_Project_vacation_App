from flask import jsonify, request
from psycopg2 import errors
from models.users_model import add_user, get_all_users, get_user_by_id, update_user, delete_user

def create_user_controller(data):
    try:
        name = data.get("name")
        email = data.get("email")
        password = data.get("password")
        role_id = data.get("role_id", 2)  # Default role_id 2 para usuarios normales
        birthday = data.get("birthday")
        address = data.get("address")
        
        if not name or not email or not password:
            return jsonify({"error": "Faltan campos requeridos"}), 400

        user_id = add_user(name, email, password, role_id, birthday, address)
        if user_id:
            return jsonify({
                "message": "Usuario registrado exitosamente!",
                "user_id": user_id
            }), 201
            
    except errors.UniqueViolation:
        return jsonify({"error": "El email ya está registrado"}), 409
    except Exception as e:
        print(f"Error en create_user_controller: {str(e)}")
        return jsonify({"error": "Error al registrar usuario"}), 500

# ... resto de tus controladores sin cambios ...

# Controller to fetch all users
def fetch_all_users_controller():
    users = get_all_users()
    user_list = [{"id": u[0], "name": u[1], "email": u[2], "role_id": u[4]} for u in users]
    return jsonify(user_list), 200

# Controller to fetch a user by ID
def fetch_user_by_id_controller(user_id):
    user = get_user_by_id(user_id)
    if user:
        user_data = {"id": user[0], "name": user[1], "email": user[2], "role_id": user[4]}
        return jsonify(user_data), 200
    return jsonify({"error": "User not found"}), 404

# Controller to update a user
def update_user_controller(user_id, data):
    updated = update_user(user_id, data.get("name"), data.get("email"), data.get("password"), data.get("role_id"), data.get("birthday"), data.get("address"))
    if updated:
        return jsonify({"message": "User updated successfully!"}), 200
    return jsonify({"error": "User not found"}), 404

# Controller to delete a user
def delete_user_controller(user_id):
    deleted = delete_user(user_id)
    if deleted:
        return jsonify({"message": "User deleted successfully!"}), 200
    return jsonify({"error": "User not found"}), 404
