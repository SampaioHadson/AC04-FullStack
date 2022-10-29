from flask import render_template, request, jsonify
from services import noteService
from flask import Blueprint

homeRoutes = Blueprint('homeRoutes', __name__)


@homeRoutes.route("/")
def index():
    items = noteService.get_all()
    return render_template("index.html", items=items)
