from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    
    # Registering blueprints
    from engine.routes import engine_bp
    app.register_blueprint(engine_bp)

    return app