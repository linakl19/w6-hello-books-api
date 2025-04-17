from flask import Flask
from .routes.book_routes import books_bp

def create_app():
    app = Flask(__name__)

    # Register books blueprint -> our bp is recognized by our Flask app
    app.register_blueprint(books_bp)

    return app