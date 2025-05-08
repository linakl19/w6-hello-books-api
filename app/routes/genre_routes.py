from app.models.genre import Genre
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