from flask import Flask, render_template
from videoclub import VideoClub


app = Flask(__name__)

@app.route('/')
def videoclub():
    return render_template('ola')


@app.route('/peliculas')
def peliculas():
    return render_template('peliculas')
  

@app.route('/clientes')
def clientes():
    return render_template('clientes')

@app.route('/alquileres')
def alquileres():
    return render_template('alquileres')



