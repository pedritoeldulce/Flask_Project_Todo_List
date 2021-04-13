from flask import Blueprint
from flask import render_template, request
from flask import flash


from app.forms import LoginForm, RegisterForm
#from app.models import Users
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

    if request.method == 'POST' and form.validate():
        print('Nueva sesion creada')
        print(form.username.data, form.password.data)
    return render_template('auth/login.html', title='Login', form=form)


@page.route('/register', methods=['GET', 'POST'])
def register():
    from app.models import Users  # corregir el llamado de forma global
    form = RegisterForm(request.form)

    if request.method == 'POST':
        if form.validate():
            user = Users.create_element(form.username.data, form.password.data, form.email.data)
            flash('USuario registrado exitosamente.')
            
            # print("Usuario creado de forma exitosa")
            # print(user.id)

    return render_template('auth/register.html', title='Registro', form=form)