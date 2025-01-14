from flask import jsonify
from models.roles_model import add_role, get_all_roles, get_role_by_id, update_role, delete_role

# Create a new role
def create_role(data):
    name = data.get("name")
    if not name:
        return jsonify({"error": "Role name is required"}), 400

    role_id = add_role(name)
    if role_id:
        return jsonify({"message": "Role added successfully!", "role_id": role_id}), 201
    else:
        return jsonify({"error": "Failed to add role"}), 500

# Get all roles
def fetch_all_roles():
    roles = get_all_roles()
    return jsonify([{"id": role[0], "name": role[1]} for role in roles]), 200

# Get role by ID
def fetch_role_by_id(role_id):
    role = get_role_by_id(role_id)
    if role:
        return jsonify({"id": role[0], "name": role[1]}), 200
    else:
        return jsonify({"error": "Role not found"}), 404

# Update a role
def update_role_controller(role_id, data):
    name = data.get("name")
    if not name:
        return jsonify({"error": "Role name is required"}), 400

    updated = update_role(role_id, name)
    if updated:
        return jsonify({"message": "Role updated successfully!"}), 200
    else:
        return jsonify({"error": "Role not found"}), 404

# Delete a role
def delete_role_controller(role_id):
    deleted = delete_role(role_id)
    if deleted:
        return jsonify({"message": "Role deleted successfully!"}), 200
    else:
        return jsonify({"error": "Role not found"}), 404
