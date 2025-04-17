from flask import Blueprint

# Create a Blueprint
hello_world_bp = Blueprint("hello_world", __name__)

# Create endpoint
@hello_world_bp.get("/")
def say_hello_world():
    return "Hello, World!"

"""
Use the Blueprint hello_world_bp
Match the route "/hello/JSON"
Match the HTTP method .get()
Give a response 200 OK
The HTTP response body should be a dictionary.
"""
@hello_world_bp.get("/hello/JSON")
def say_hello_json():
    return {
        "name": "Ada Lovelace",
        "message": "Hello!",
        "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
    }
