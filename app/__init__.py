from flask import Flask
from .routes.book_routes import books_bp
from .db import db, migrate

def create_app():
    app = Flask(__name__)

    # 1. hide a warning about a feature in SQLAlchemy that we won't be using
    # 2. the connection string for our database
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/hello_books_development'

    # Connects db and migrate to our Flask app
    db.init_app(app)
    migrate.init_app(app, db)

    # Register books blueprint -> our bp is recognized by our Flask app
    app.register_blueprint(books_bp)

    return app