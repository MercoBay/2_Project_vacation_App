from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from routes.country_routes import country_bp  # Rutas de countries
from routes.likes_routes import likes_bp  # Rutas de likes
from routes.users_routes import users_bp  # Rutas de users
from routes.roles_routes import roles_bp  # Rutas de roles
from routes.vacations_routes import vacations_bp  # Rutas de vacations
import os
from dotenv import load_dotenv
from datetime import timedelta

# Cargar las variables de entorno desde .env
load_dotenv()

# Crear la aplicación Flask
app = Flask(__name__)

# Configuración JWT - Clave fija simple para desarrollo
JWT_SECRET = "super_secret"  # Una clave más simple para pruebas
app.config["JWT_SECRET_KEY"] = JWT_SECRET
jwt = JWTManager(app)

# Configuración adicional de JWT
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)

# DESPUÉS configurar CORS y blueprints
CORS(app)
app.register_blueprint(country_bp)
app.register_blueprint(likes_bp)
app.register_blueprint(users_bp)
app.register_blueprint(roles_bp)
app.register_blueprint(vacations_bp)

# Ruta raíz
@app.route("/")
def home():
    return {"message": "Bienvenido a la API de Vacaciones"}, 200

# Iniciar la aplicación
if __name__ == "__main__":
    app.run(debug=True)

