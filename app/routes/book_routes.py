from flask import Blueprint, Response, abort, make_response, request
from app.models.book import Book
from ..db import db


books_bp = Blueprint("books_bp", __name__, url_prefix="/books")


# POST one
@books_bp.post("")
def create_book():
    # Handling the incomming data
    request_body = request.get_json()

    try:
        new_book = Book.from_dict(request_body)

    except KeyError as error:
        response = {"message": f"Invalid request: missing {error.args[0]}"}
        abort(make_response(response, 400))

    db.session.add(new_book)
    db.session.commit()

    # Returning a response
    response = {
        "id": new_book.id,
        "title": new_book.title,
        "description": new_book.description,
    }
    return response, 201


#GET all
@books_bp.get("")
def get_all_books():
    # select all books
    query = db.select(Book)

	# select books with matching title
    title_param = request.args.get("title")
    if title_param:
        query = query.where(Book.title.ilike(f"%{title_param}%"))
    
    # select books with matching description
    description_param = request.args.get("description")
    if description_param:
        query = query.where(Book.description.ilike(f"%{description_param}%"))
	
    query = query.order_by(Book.id)
    books = db.session.scalars(query)
    #can also be written as:
	# books = db.session.scalars(query.order_by(Book.id))

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


# GET one
@books_bp.get("/<book_id>")
def gets_one_book(book_id):
    book = validate_book(book_id)

    return {
        "id": book.id,
        "title": book.title,
        "description": book.description,
    }


# UPDATE one
@books_bp.put("/<book_id>")
def update_book(book_id):
    book = validate_book(book_id)
    request_body = request.get_json()

    book.title = request_body["title"]
    book.description = request_body["description"]
    db.session.commit()

    return Response(status=204, mimetype="application/json")


# DELETE one
@books_bp.delete("/<book_id>")
def delete_book(book_id):
    book = validate_book(book_id)
    db.session.delete(book)
    db.session.commit()

    return Response(status=204, mimetype="application/json")


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