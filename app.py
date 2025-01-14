from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from routes.country_routes import country_bp
from routes.likes_routes import likes_bp
from routes.users_routes import users_bp
from routes.roles_routes import roles_bp
from routes.vacations_routes import vacations_bp
import os
from dotenv import load_dotenv
from routes.auth_routes import auth_bp

# Cargar las variables de entorno desde .env
load_dotenv()

# Crear la aplicación Flask
app = Flask(__name__)

# Configuración de la clave secreta para JWT
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "default_secret_key")
jwt = JWTManager(app)

# Configuración específica de CORS
CORS(app, resources={
    r"/*": {
        "origins": ["http://localhost:5173"],  # URL de tu frontend
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"],
        "supports_credentials": True
    }
})

# Registrar los blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(country_bp)
app.register_blueprint(likes_bp)
app.register_blueprint(users_bp)
app.register_blueprint(roles_bp)
app.register_blueprint(vacations_bp)

@app.route("/")
def home():
    return {"message": "Bienvenido a la API de Vacaciones"}, 200

if __name__ == "__main__":
    app.run(debug=True)