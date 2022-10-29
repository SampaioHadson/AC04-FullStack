from database import db
from entities.note import Note
from repositories import noteRepository
from services import noteService

from flask import Flask, render_template

app = Flask(__name__)
db.start()


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
