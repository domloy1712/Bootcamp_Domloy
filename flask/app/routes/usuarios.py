
from flask import Blueprint, render_template, request, redirect,url_for
from app import db
from app.models import Usuario

usuarios_bp = Blueprint('usuarios', __name__,url_prefix='/usuarios')

@usuarios_bp.route('/')
def lista():
   usuarios = Usuario.query.all()
   return render_template('usuarios/lista.html', usuarios=usuarios)

@usuarios_bp.route('/crear', methods=['GET', 'POST'])
def crear():
   if request.method == 'POST':
      nombre = request.form['nombre']
      email = request.form['email']
      nuevo = Usuario(nombre=nombre, email=email)
      db.session.add(nuevo)
      db.session.commit()
      return redirect(url_for('usuarios.lista'))
   return render_template('usuarios/formulario.html')

@usuarios_bp.route('/eliminar/<int:id>')
def eliminar(id):    
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    return redirect(url_for('usuarios.lista'))