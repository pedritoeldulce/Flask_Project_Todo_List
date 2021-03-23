from wtforms import Form
from wtforms import StringField, PasswordField, BooleanField

from wtforms import validators
from wtforms.fields.html5 import EmailField


class LoginForm(Form):
    username = StringField('Username', [validators.length(min=4, max=50, message="El username se encuentra fuera de rango"), validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired(message='El password es requerido')])


class RegisterForm(Form):
    username = StringField('Username', [validators.length(min=4, max=50), validators.DataRequired(message='El usuario es requerido')])
    email = EmailField('Correo electrònico',[
        validators.length(min=6, max=100),
        validators.DataRequired(message='El email es requerido'),
        validators.Email(message='Ingrese un email vàlido')
    ])
    password = PasswordField('Password', [
        validators.DataRequired(message='El password es requerido'),
        validators.EqualTo('confirm_password', message='La contraseña no coincide')
    ])
    confirm_password = PasswordField('Confirm Password')
    accept = BooleanField([
        validators.DataRequired()
    ])