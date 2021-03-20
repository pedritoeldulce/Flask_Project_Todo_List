from flask import Flask
from .views import page  # Importamos todas las rutas almancenadas en page
from flask_bootstrap import Bootstrap  # importamos la libreria Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap()  # creamos una instancia de bootstrap


def create_app(config):  # Indicamos que la funcion create_app reciba un parametro: config
    app.config.from_object(config)  # Indicamos al aervidor que utilice nuestras configuraciones de 'config'
    bootstrap.init_app(app)  # Le indicamos al servidor que use bootstrap, esto se harà en los templates (herencia)
    app.register_blueprint(page)  # vamos a indicar al servidor con que rutas se va a trabajar
    return app