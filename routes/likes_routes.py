from flask import Blueprint, request
from controllers.likes_controller import create_like, fetch_all_likes, fetch_likes_by_user, remove_like
from utils.auth import verify_simple_token

# Define the Blueprint for likes routes
likes_bp = Blueprint("likes_routes", __name__)

# Route to add a like
@likes_bp.route("/likes", methods=["POST"])
def add_like_route():
    auth_token = request.headers.get('X-Auth-Token')
    if not auth_token:
        return {"error": "Authentication required"}, 401
        
    # Verificar token simple
    user_id = verify_simple_token(auth_token)
    if not user_id:
        return {"error": "Invalid token"}, 401
        
    data = request.json
    data["user_id"] = user_id
    return create_like(data)

# Route to get all likes
@likes_bp.route("/likes", methods=["GET"])
def get_all_likes_route():
    return fetch_all_likes()

# Route to get all likes for a specific user
@likes_bp.route("/likes/user/<int:user_id>", methods=["GET"])
def get_likes_by_user_route(user_id):
    return fetch_likes_by_user(user_id)

# Route to delete a like
@likes_bp.route("/likes", methods=["DELETE"])
def delete_like_route():
    data = request.json
    return remove_like(data.get("user_id"), data.get("vacation_id"))
