# models/db_config.py
import psycopg2
import os
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

# Configuración de la base de datos desde .env
DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "sslmode": "require"  # Opcional: Si Neon requiere SSL
}

def get_db_connection():
    return psycopg2.connect(**DB_CONFIG)
