from flask import Blueprint, abort, make_response, request
from app.models.book import Book
from ..db import db

books_bp = Blueprint("books_bp", __name__, url_prefix="/books")

@books_bp.post("")
def create_book():
    # Handling the incomming data
    request_body = request.get_json()
    title = request_body["title"]
    description = request_body["description"]

    # Creating and saving the new book
    new_book = Book(title=title, description=description)
    db.session.add(new_book)
    db.session.commit()

    # Returning a response
    response = {
        "id": new_book.id,
        "title": new_book.title,
        "description": new_book.description,
    }
    return response, 201

#Getting all books endpoint
@books_bp.get("")
def get_all_books():
    query = db.select(Book).order_by(Book.id)
    books = db.session.scalars(query)
    # We could also write the line above as:
    # books = db.session.execute(query).scalars()

    books_response = []
    for book in books:
        books_response.append(
            {
                "id": book.id,
                "title": book.title,
                "description": book.description
            }
        )
    return books_response

# Getting a single book endpoint
@books_bp.get("/<book_id>")
def gets_one_book(book_id):
    book = validate_book(book_id)

    return {
        "id": book.id,
        "title": book.title,
        "description": book.description,
    }

# Helper function to validate book_id
def validate_book(book_id):
    try:
        book_id = int(book_id)
    except:
        response = {"message": f"Book with id:{book_id} is invalid"}
        abort(make_response(response, 400))

    query = db.select(Book).where(Book.id == book_id)
    book = db.session.scalar(query)

    if not book:
        response = {"message": f"Book with id:{book_id} was not found"}
        abort(make_response(response, 404))
    
    return book



# from flask import Blueprint, abort, make_response
# from app.models.book import books

# books_bp = Blueprint("books_bp", __name__, url_prefix="/books")

# @books_bp.get("")
# def get_all_books():
#     books_response = []
#     for book in books:
#         books_response.append(
#             {
#                 "id":book.id,
#                 "title": book.title,
#                 "description": book.description
#             }
#         )
#     return books_response

# # Getting a single book endpoint
# @books_bp.get("/<book_id>")
# def gets_one_book(book_id):
#     book = validate_book(book_id)

#     return dict(
#         id = book.id,
#         title = book.title,
#         description = book.description,
#     )

# # Helper function to validate book_id
# def validate_book(book_id):
#     try:
#         book_id = int(book_id)
#     except:
#         response = {"message": f"Book with id:{book_id} is invalid"}
#         abort(make_response(response, 400))

#     for book in books:
#         if book.id == book_id:
#             return book
        
#     response = {"message": f"Book with id:{book_id} was not found"}
#     abort(make_response(response, 404))