from database import db
from flask import Flask
from routes.homeRoutes import homeRoutes
from routes.noteRoutes import noteRoutes

app = Flask(__name__)
app.register_blueprint(homeRoutes)
app.register_blueprint(noteRoutes)
db.start()

if __name__ == '__main__':
    app.debug = True
    app.run()
