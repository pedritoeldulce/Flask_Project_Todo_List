from flask import Flask
from .views import page # Importamos todas las rutas almancenadas en page

app = Flask(__name__)


def create_app(config):  # Indicamos que la funcion create_app reciba un parametro: config
    app.config.from_object(config)  # Indicamos al aervidor que utilice nuestras configuraciones de 'config'
    app.register_blueprint(page) # vamos a indicar al servidor con que rutas se va a trabajar
    return app