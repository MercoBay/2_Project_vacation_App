from models.db_config import get_db_connection

# Add a new role
def add_role(name):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO roles (name) VALUES (%s) RETURNING id", (name,))
        role_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return role_id
    except Exception as e:
        print(f"Error adding role: {e}")
        return None

# Get all roles
def get_all_roles():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM roles")
        roles = cur.fetchall()
        cur.close()
        conn.close()
        return roles
    except Exception as e:
        print(f"Error fetching roles: {e}")
        return []

# Get a role by its ID
def get_role_by_id(role_id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM roles WHERE id = %s", (role_id,))
        role = cur.fetchone()
        cur.close()
        conn.close()
        return role
    except Exception as e:
        print(f"Error fetching role by ID: {e}")
        return None

# Update a role
def update_role(role_id, name):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("UPDATE roles SET name = %s WHERE id = %s", (name, role_id))
        conn.commit()
        updated = cur.rowcount > 0  # Check if at least one row was updated
        cur.close()
        conn.close()
        return updated
    except Exception as e:
        print(f"Error updating role: {e}")
        return False

# Delete a role
def delete_role(role_id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM roles WHERE id = %s", (role_id,))
        conn.commit()
        deleted = cur.rowcount > 0  # Check if at least one row was deleted
        cur.close()
        conn.close()
        return deleted
    except Exception as e:
        print(f"Error deleting role: {e}")
        return False
