from flask import jsonify, request
from models.users_model import add_user, get_all_users, get_user_by_id, update_user, delete_user, get_user_by_email
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

# Controller to create a user
def create_user_controller(data):
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    role_id = data.get("role_id")
    birthday = data.get("birthday")
    address = data.get("address")
    
    if not name or not email or not password or not role_id:
        return jsonify({"error": "Missing required fields"}), 400

    user_id = add_user(name, email, password, role_id, birthday, address)
    if user_id:
        return jsonify({"message": "User added successfully!", "user_id": user_id}), 201
    return jsonify({"error": "Failed to add user"}), 500

# Controller to fetch all users
def fetch_all_users_controller():
    users = get_all_users()
    user_list = [{
        "id": u[0],
        "email": u[1],
        "name": u[5],
        "role_id": u[6],
        "first_name": u[7],
        "last_name": u[8]
    } for u in users]
    return jsonify(user_list), 200

# Controller to fetch a user by ID
def fetch_user_by_id_controller(user_id):
    user = get_user_by_id(user_id)
    if user:
        user_data = {
            "id": user[0],
            "email": user[1],
            "name": user[5],
            "role_id": user[6],
            "first_name": user[7],
            "last_name": user[8]
        }
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

def register_user_controller(data):
    # Obtener datos básicos
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    role_id = data.get("role_id", 2)  # Default role_id 2
    birthday = data.get("birthday")    # Opcional
    address = data.get("address")      # Opcional
    
    if not name or not email or not password:
        return jsonify({"error": "Missing required fields"}), 400

    # Verificar si el usuario ya existe
    existing_user = get_user_by_email(email)
    if existing_user:
        return jsonify({"error": "Email already registered"}), 400

    # Hash del password
    hashed_password = generate_password_hash(password)
    
    # Usar la función add_user con los campos correctos
    user_id = add_user(
        name=name,
        email=email,
        password=hashed_password,
        role_id=role_id,
        birthday=birthday,
        address=address
    )

    if user_id:
        return jsonify({
            "message": "User registered successfully!",
            "user_id": user_id
        }), 201
    return jsonify({"error": "Registration failed"}), 500

def login_user_controller(data):
    email = data.get("email")
    password = data.get("password")
    
    if not email or not password:
        return jsonify({"error": "Missing email or password"}), 400

    user = get_user_by_email(email)
    if not user:
        return jsonify({"error": "User not found"}), 404

    if not check_password_hash(user[2], password):  # password está en índice 2
        return jsonify({"error": "Invalid password"}), 401

    return jsonify({
        "message": "Login successful",
        "token": str(user[0]),  # user_id como token
        "user": {
            "id": user[0],
            "email": user[1],
            "name": user[5]
        }
    }), 200
