import psycopg2
from models.db_config import get_db_connection

# Add a new country
def add_country(name):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO countries (name) VALUES (%s) RETURNING id", (name,))
        country_id = cur.fetchone()[0]
        conn.commit()
        return country_id
    except psycopg2.errors.UniqueViolation:
        conn.rollback()
        # Return an error message if the country name already exists
        return {"error": "This country name already exists"}, 400
    except Exception as e:
        conn.rollback()
        # Handle any other internal server error
        print(f"Error adding country: {e}")
        return {"error": "Internal server error"}, 500
    finally:
        # Always close the cursor and the connection
        cur.close()
        conn.close()

# Get all countries
def get_all_countries():
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM countries")
        countries = cur.fetchall()
        return countries
    except Exception as e:
        # Handle errors during the fetch process
        print(f"Error fetching countries: {e}")
        return {"error": "Internal server error"}, 500
    finally:
        cur.close()
        conn.close()

# Get a country by its ID
def get_country_by_id(country_id):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM countries WHERE id = %s", (country_id,))
        country = cur.fetchone()
        if not country:
            # Return an error if the country does not exist
            return {"error": "Country not found"}, 404
        return country
    except Exception as e:
        # Handle errors when retrieving the country
        print(f"Error fetching country by ID: {e}")
        return {"error": "Internal server error"}, 500
    finally:
        cur.close()
        conn.close()

# Update a country
def update_country(country_id, name):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        # Check if the new country name already exists in another entry
        cur.execute("SELECT id FROM countries WHERE name = %s", (name,))
        existing_country = cur.fetchone()
        if existing_country and existing_country[0] != country_id:
            return {"error": "This country name already exists"}, 400

        cur.execute("UPDATE countries SET name = %s WHERE id = %s", (name, country_id))
        conn.commit()
        updated = cur.rowcount > 0  # Check if at least one row was updated
        if updated:
            return {"message": "Country updated successfully"}, 200
        else:
            return {"error": "Country not found"}, 404
    except Exception as e:
        conn.rollback()
        # Handle errors during the update process
        print(f"Error updating country: {e}")
        return {"error": "Internal server error"}, 500
    finally:
        cur.close()
        conn.close()

# Delete a country
def delete_country(country_id):
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute("DELETE FROM countries WHERE id = %s", (country_id,))
        conn.commit()
        deleted = cur.rowcount > 0  # Check if at least one row was deleted
        if deleted:
            return {"message": "Country deleted successfully"}, 200
        else:
            return {"error": "Country not found"}, 404
    except Exception as e:
        conn.rollback()
        # Handle errors during the deletion process
        print(f"Error deleting country: {e}")
        return {"error": "Internal server error"}, 500
    finally:
        cur.close()
        conn.close()

