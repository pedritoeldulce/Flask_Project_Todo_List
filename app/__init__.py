from flask import Flask

from .views import page  # Importamos todas las rutas almancenadas en page
from flask_bootstrap import Bootstrap  # importamos la libreria Bootstrap
from flask_wtf.csrf import CSRFProtect

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)
from .models import Users
bootstrap = Bootstrap()  # creamos una instancia de bootstrap
csrf = CSRFProtect()  # instanciamos


def create_app(config):  # Indicamos que la funcion create_app reciba un parametro: config
    app.config.from_object(config)  # Indicamos al aervidor que utilice nuestras configuraciones de 'config'

    csrf.init_app(app)
    bootstrap.init_app(app)  # Le indicamos al servidor que use bootstrap, esto se harà en los templates (herencia)
    app.register_blueprint(page)  # vamos a indicar al servidor con que rutas se va a trabajar


    with app.app_context():

        db.init_app(app) # realizar la conexoin mediante un contexto
        db.create_all()

    return app