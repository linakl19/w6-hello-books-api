# Book class to represent book data
class Book:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description


# 	List of hardcoded Book instances which acts as our stored data for now
books = [
    Book(1, "Fictional Book", "A fantasy novel set in an imaginary world."),
    Book(2, "Wheel of Time", "A fantasy novel set in an imaginary world."),
    Book(3, "Fictional Book Title", "A fantasy novel set in an imaginary world.")
]