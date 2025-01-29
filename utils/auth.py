def verify_simple_token(token):
    try:
        # Simple verificación: el token es el user_id
        return int(token)
    except:
        return None 