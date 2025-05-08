from app.models.genre import Genre
from .route_utilities import validate_model, create_model
from flask import Blueprint
from ..db import db

bp = Blueprint("genres_bp", __name__, url_prefix="/genres")

