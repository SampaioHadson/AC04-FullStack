from flask import render_template, request, jsonify
from entities.note import Note
from services import noteService
from flask import Blueprint

noteRoutes = Blueprint('noteRoutes', __name__)


@noteRoutes.route("/add", methods=['POST'])
def add():
    result = request.json
    note = Note()
    note.description = result["description"]
    note.name = result["name"]
    noteService.add(note)
    return {}


@noteRoutes.route("/delete/<id>", methods=['POST'])
def delete(id):
    noteService.delete(id)
    return {}
