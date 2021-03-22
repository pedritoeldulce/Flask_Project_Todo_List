from flask import Blueprint
from flask import render_template, request


from forms import LoginForm  # Importamos el LoginForm

page = Blueprint('page', __name__)  #(nombre del contexto, contexto en el cual se crea la instancia)


@page.app_errorhandler(404)  #Error de pàgina no encontrada
def page_not_found(error):
    return render_template('errors/404.html'), 404


@page.route('/')
def index():
    return render_template('index.html', title="Index")


@page.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)  # instanciamos form y lo enviamos al template

    if request.method == 'POST':
        print('Nueva sesion creada')
        print(form.username.data, form.password.data)
    return render_template('auth/login.html', title='Login', form=form)