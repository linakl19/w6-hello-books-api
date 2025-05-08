from flask import Blueprint, Response, abort, make_response, request
from app.models.book import Book
from ..db import db
from app.routes.route_utilities import validate_model, create_model, get_models_with_filters


bp = Blueprint("book_bp", __name__, url_prefix="/books")


# POST one
@bp.post("")
def create_book():
    # Handling the incomming data
    request_body = request.get_json()
    return create_model(Book, request_body)


#GET all
@bp.get("")
def get_all_books():
    return get_models_with_filters(Book, request.args)


# GET one
@bp.get("/<book_id>")
def gets_one_book(book_id):
    book = validate_model(Book, book_id)
    return book.to_dict()


# UPDATE one
@bp.put("/<book_id>")
def update_book(book_id):
    book = validate_model(Book, book_id)
    request_body = request.get_json()

    book.title = request_body["title"]
    book.description = request_body["description"]
    db.session.commit()

    return Response(status=204, mimetype="application/json")


# DELETE one
@bp.delete("/<book_id>")
def delete_book(book_id):
    book = validate_model(Book, book_id)
    db.session.delete(book)
    db.session.commit()

    return Response(status=204, mimetype="application/json")


