from models.db_config import get_db_connection

# Add a user
def add_user(name, email, password, role_id, birthday=None, address=None):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO users (name, email, password, role_id, birthday, address) 
            VALUES (%s, %s, %s, %s, %s, %s) RETURNING id
        """, (name, email, password, role_id, birthday, address))
        user_id = cur.fetchone()[0]
        conn.commit()
        return user_id
    except Exception as e:
        print("Error:", e)
        return None
    finally:
        cur.close()
        conn.close()

# Get all users
def get_all_users():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users")
        users = cur.fetchall()
        return users
    except Exception as e:
        print("Error:", e)
        return []
    finally:
        cur.close()
        conn.close()

# Get a user by ID
def get_user_by_id(user_id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user = cur.fetchone()
        return user
    except Exception as e:
        print("Error:", e)
        return None
    finally:
        cur.close()
        conn.close()

# Update a user
def update_user(user_id, name=None, email=None, password=None, role_id=None, birthday=None, address=None):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            UPDATE users 
            SET name = COALESCE(%s, name), 
                email = COALESCE(%s, email), 
                password = COALESCE(%s, password), 
                role_id = COALESCE(%s, role_id),
                birthday = COALESCE(%s, birthday), 
                address = COALESCE(%s, address)
            WHERE id = %s
        """, (name, email, password, role_id, birthday, address, user_id))
        conn.commit()
        return cur.rowcount > 0  # True if at least one row was updated
    except Exception as e:
        print("Error:", e)
        return False
    finally:
        cur.close()
        conn.close()

# Delete a user
def delete_user(user_id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
        conn.commit()
        return cur.rowcount > 0  # True if at least one row was deleted
    except Exception as e:
        print("Error:", e)
        return False
    finally:
        cur.close()
        conn.close()
