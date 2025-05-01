from sqlalchemy.orm import Mapped, mapped_column
from ..db import db

class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    description: Mapped[str]

    # Instance methods
    def to_dict(self):
        book_as_dict = {}
        book_as_dict["id"] = self.id
        book_as_dict["title"] = self.title
        book_as_dict["description"] = self.description

        return book_as_dict

    # Class method - convenience initializer
    @classmethod
    def from_dict(cls, book_data):
        new_book = Book(title=book_data["title"],
                        description=book_data["description"])

        return new_book


# # Book class to represent book data
# class Book:
#     def __init__(self, id, title, description):
#         self.id = id
#         self.title = title
#         self.description = description

# # 	List of hardcoded Book instances which acts as our stored data for now
# books = [
#     Book(1, "Fictional Book", "A fantasy novel set in an imaginary world."),
#     Book(2, "Wheel of Time", "A fantasy novel set in an imaginary world."),
#     Book(3, "Fictional Book Title", "A fantasy novel set in an imaginary world.")
# ]