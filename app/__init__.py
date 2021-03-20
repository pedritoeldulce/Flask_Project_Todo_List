from flask import Flask
from .views import page # Importamos todas las rutas almancenadas en page

app = Flask(__name__)


def create_app():
    app.register_blueprint(page) # vamos a indicar al servidor con que rutas se va a trabajar
    return app