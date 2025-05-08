from app.models.genre import Genre
from app.models.book import Book
from .route_utilities import validate_model, create_model, get_models_with_filters
from flask import Blueprint, request
from ..db import db

bp = Blueprint("genres_bp", __name__, url_prefix="/genres")


@bp.post("")
def create_genre():
    request_body = request.get_json()
    return create_model(Genre, request_body)

@bp.get("")
def get_all_genres():
    return get_models_with_filters(Genre, request.args)


# Nested routes - many to many relationship
@bp.post("/<genre_id>/books")
def post_book_with_genre_id(genre_id):
    genre = validate_model(Genre, genre_id)
    request_body = request.get_json()
    request_body["genres"] = [genre]

    return create_model(Book, request_body)


@bp.get("/<genre_id>/books")
def get_books_with_genre_id(genre_id):
    genre = validate_model(Genre, genre_id)
    return [book.to_dict() for book in genre.books]