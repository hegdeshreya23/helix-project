from flask import Flask, jsonify
from flask_cors import CORS
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize CORS
    CORS(app)
    
    # Root route for testing
    @app.route('/')
    def health_check():
        return jsonify({"status": "healthy", "message": "Helix HR Agent API is running"})

    # Register blueprints without prefix
    from .routes.chat import chat_bp
    app.register_blueprint(chat_bp)
    
    print("Registered routes:")
    print(app.url_map)  # This will print all registered routes
    
    return app