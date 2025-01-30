from models.db_config import get_db_connection

# Add a vacation
def add_vacation(country_id, description, start_date, end_date, price, image_url):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO vacations (country_id, description, start_date, end_date, price, image_url)
            VALUES (%s, %s, %s, %s, %s, %s) RETURNING id
        """, (country_id, description, start_date, end_date, price, image_url))
        vacation_id = cur.fetchone()[0]
        conn.commit()
        return vacation_id
    except Exception as e:
        print("Error:", e)
        return None
    finally:
        cur.close()
        conn.close()

# Get all vacations
def get_all_vacations(user_id=None):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        query = """
            SELECT 
                v.*,
                COUNT(DISTINCT l.user_id) as followers_amount,
                CASE WHEN EXISTS (
                    SELECT 1 FROM likes l2 
                    WHERE l2.vacation_id = v.id AND l2.user_id = %s
                ) THEN true ELSE false END as user_following
            FROM vacations v
            LEFT JOIN likes l ON v.id = l.vacation_id
            GROUP BY v.id
            ORDER BY v.id
        """
        
        cur.execute(query, (user_id,))
        vacations = cur.fetchall()
        return vacations
    except Exception as e:
        print("Error:", e)
        return []
    finally:
        cur.close()
        conn.close()

# Get vacation by ID
def get_vacation_by_id(vacation_id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM vacations WHERE id = %s", (vacation_id,))
        vacation = cur.fetchone()
        return vacation
    except Exception as e:
        print("Error:", e)
        return None
    finally:
        cur.close()
        conn.close()

# Update a vacation
def update_vacation(vacation_id, country_id=None, description=None, start_date=None, end_date=None, price=None, image_url=None):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            UPDATE vacations
            SET country_id = COALESCE(%s, country_id),
                description = COALESCE(%s, description),
                start_date = COALESCE(%s, start_date),
                end_date = COALESCE(%s, end_date),
                price = COALESCE(%s, price),
                image_url = COALESCE(%s, image_url)
            WHERE id = %s
        """, (country_id, description, start_date, end_date, price, image_url, vacation_id))
        conn.commit()
        return cur.rowcount > 0
    except Exception as e:
        print("Error:", e)
        return False
    finally:
        cur.close()
        conn.close()

# Delete a vacation
def delete_vacation(vacation_id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM vacations WHERE id = %s", (vacation_id,))
        conn.commit()
        return cur.rowcount > 0
    except Exception as e:
        print("Error:", e)
        return False
    finally:
        cur.close()
        conn.close()

# from models.db_config import get_db_connection

# # Add a vacation
# def add_vacation(country_id, description, start_date, end_date, price, image_url):
#     try:
#         conn = get_db_connection()
#         cur = conn.cursor()
#         cur.execute("""
#             INSERT INTO vacations (country_id, description, start_date, end_date, price, image_url)
#             VALUES (%s, %s, %s, %s, %s, %s) RETURNING id
#         """, (country_id, description, start_date, end_date, price, image_url))
#         vacation_id = cur.fetchone()[0]
#         conn.commit()
#         return vacation_id
#     except Exception as e:
#         print("Error:", e)
#         return None
#     finally:
#         cur.close()
#         conn.close()

# # Get all vacations
# def get_all_vacations():
#     try:
#         conn = get_db_connection()
#         cur = conn.cursor()
#         cur.execute("SELECT * FROM vacations")
#         vacations = cur.fetchall()
#         return vacations
#     except Exception as e:
#         print("Error:", e)
#         return []
#     finally:
#         cur.close()
#         conn.close()

# # Get vacation by ID
# def get_vacation_by_id(vacation_id):
#     try:
#         conn = get_db_connection()
#         cur = conn.cursor()
#         cur.execute("SELECT * FROM vacations WHERE id = %s", (vacation_id,))
#         vacation = cur.fetchone()
#         return vacation
#     except Exception as e:
#         print("Error:", e)
#         return None
#     finally:
#         cur.close()
#         conn.close()

# # Update a vacation
# def update_vacation(vacation_id, country_id=None, description=None, start_date=None, end_date=None, price=None, image_url=None):
#     try:
#         conn = get_db_connection()
#         cur = conn.cursor()
#         cur.execute("""
#             UPDATE vacations
#             SET country_id = COALESCE(%s, country_id),
#                 description = COALESCE(%s, description),
#                 start_date = COALESCE(%s, start_date),
#                 end_date = COALESCE(%s, end_date),
#                 price = COALESCE(%s, price),
#                 image_url = COALESCE(%s, image_url)
#             WHERE id = %s
#         """, (country_id, description, start_date, end_date, price, image_url, vacation_id))
#         conn.commit()
#         return cur.rowcount > 0
#     except Exception as e:
#         print("Error:", e)
#         return False
#     finally:
#         cur.close()
#         conn.close()

# # Delete a vacation
# def delete_vacation(vacation_id):
#     try:
#         conn = get_db_connection()
#         cur = conn.cursor()
#         cur.execute("DELETE FROM vacations WHERE id = %s", (vacation_id,))
#         conn.commit()
#         return cur.rowcount > 0
#     except Exception as e:
#         print("Error:", e)
#         return False
#     finally:
#         cur.close()
#         conn.close()
