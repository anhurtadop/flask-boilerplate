"""Index Routes"""
from flask import Blueprint

from ..controllers.index_controller import IndexController

index_route = Blueprint("index_blueprint", __name__)


@index_route.route("/", methods=["GET"])
def index():
    """index route : index"""
    return IndexController().index()
