from queue import Empty
from entities.note import Note
from repositories import noteRepository


def add(note: Note):
    if not note.description or note.description == "":
        raise Exception("Descrição é obrigatório.")

    if not note.name or note.name == "":
        raise Exception("Nome é obrigatório.")

    if len(note.name) > 120:
        raise Exception("Nome deve ter no máximo 120 caracteres.")

    noteRepository.add(note)


def delete(id):
    noteRepository.delete(id)


def get_all():
    return noteRepository.get_all()
