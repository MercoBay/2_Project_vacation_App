from flask import Blueprint, request
from controllers.likes_controller import create_like, fetch_all_likes, fetch_likes_by_user, remove_like

# Define the Blueprint for likes routes
likes_bp = Blueprint("likes_routes", __name__)

# Route to add a like
@likes_bp.route("/likes", methods=["POST"])
def add_like_route():
    return create_like(request.json)

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
    user_id = data.get("user_id")
    vacation_id = data.get("vacation_id")
    if not user_id or not vacation_id:
        return {"error": "user_id and vacation_id are required"}, 400
    return remove_like(user_id, vacation_id)
