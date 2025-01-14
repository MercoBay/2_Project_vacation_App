from flask import jsonify
from models.likes_model import add_like, get_all_likes, get_likes_by_user, delete_like

# Controller to add a like
def create_like(data):
    user_id = data.get("user_id")
    vacation_id = data.get("vacation_id")
    if not user_id or not vacation_id:
        return jsonify({"error": "user_id and vacation_id are required"}), 400

    result = add_like(user_id, vacation_id)
    return jsonify(result), result[1] if isinstance(result, tuple) else 201

# Controller to get all likes
def fetch_all_likes():
    result = get_all_likes()
    return jsonify(result[0]), result[1]

# Controller to get likes for a specific user
def fetch_likes_by_user(user_id):
    result = get_likes_by_user(user_id)
    return jsonify(result[0] if isinstance(result, tuple) else result), result[1] if isinstance(result, tuple) else 404

# Controller to delete a like
def remove_like(user_id, vacation_id):
    result = delete_like(user_id, vacation_id)
    return jsonify(result), result[1] if isinstance(result, tuple) else 200
