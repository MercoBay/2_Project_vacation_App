from functools import wraps
from flask import request, jsonify
from models.db_config import get_db_connection

def verify_simple_token(token):
    try:
        return int(token)
    except:
        return None

def verify_admin_token(token):
    try:
        user_id = int(token)
        conn = get_db_connection()
        cur = conn.cursor()
        
        cur.execute("SELECT role_id FROM users WHERE id = %s", (user_id,))
        user = cur.fetchone()
        
        if user and user[0] == 8:  # role_id 8 es admin
            return user_id
        return None
    except:
        return None
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def admin_required():
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            auth_token = request.headers.get('X-Auth-Token')
            if not auth_token:
                return jsonify({"error": "Authentication required"}), 401
            
            user_id = verify_admin_token(auth_token)
            if not user_id:
                return jsonify({"error": "Admin access required"}), 403
                
            return f(*args, **kwargs)
        return decorated_function
    return decorator