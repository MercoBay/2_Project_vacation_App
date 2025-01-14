import psycopg2
from models.db_config import get_db_connection

# Add a like (user likes a vacation)
def add_like(user_id, vacation_id):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("""
            INSERT INTO likes (user_id, vacation_id)
            VALUES (%s, %s)
        """, (user_id, vacation_id))
        conn.commit()
        return {"message": "Like added successfully"}, 201
    except psycopg2.errors.UniqueViolation:
        conn.rollback()
        # Return an error if the user has already liked the vacation
        return {"error": "This like already exists"}, 400
    except Exception as e:
        conn.rollback()
        print(f"Error adding like: {e}")
        return {"error": "Internal server error"}, 500
    finally:
        cur.close()
        conn.close()

# Get all likes
def get_all_likes():
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM likes")
        likes = cur.fetchall()
        return [{"user_id": like[0], "vacation_id": like[1]} for like in likes], 200
    except Exception as e:
        print(f"Error fetching likes: {e}")
        return {"error": "Internal server error"}, 500
    finally:
        cur.close()
        conn.close()

# Get all likes by a specific user
def get_likes_by_user(user_id):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM likes WHERE user_id = %s", (user_id,))
        likes = cur.fetchall()
        if not likes:
            return {"error": "No likes found for this user"}, 404
        return [{"vacation_id": like[1]} for like in likes], 200
    except Exception as e:
        print(f"Error fetching likes for user: {e}")
        return {"error": "Internal server error"}, 500
    finally:
        cur.close()
        conn.close()

# Delete a like
def delete_like(user_id, vacation_id):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM likes WHERE user_id = %s AND vacation_id = %s", (user_id, vacation_id))
        conn.commit()
        deleted = cur.rowcount > 0
        if deleted:
            return {"message": "Like deleted successfully"}, 200
        else:
            return {"error": "Like not found"}, 404
    except Exception as e:
        conn.rollback()
        print(f"Error deleting like: {e}")
        return {"error": "Internal server error"}, 500
    finally:
        cur.close()
        conn.close()
