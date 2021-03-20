from flask import Blueprint
from flask import render_template


page = Blueprint('page', __name__) #(nombre del contexto, contexto en el cual se crea la instancia)



@page.route('/')
def index():
    return render_template('index.html')