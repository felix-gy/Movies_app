from flask import Flask, render_template, request, redirect, url_for, flash
from queries.movies import *
from queries.users import *
from queries.comments import *

app = Flask(__name__)

my_session = {'logged': False}
app.secret_key = 'clave_secreta'


@app.route('/')
def login():
  return render_template('login.html')


@app.route('/register')
def register():
  return render_template('register.html')


@app.route('/pagina_principal')
def pagina_principal():
  peliculas = all_movies()
  return render_template('test.html', peliculas=peliculas)


@app.route('/submit_register', methods=['POST'])
def submit_register():
  nombre = request.form['nombre']
  email = request.form['email']
  contraseña = request.form['password']
  insert_user(nombre, email, contraseña)
  return redirect(url_for('pagina_principal'))


@app.route('/submit_login', methods=['POST'])
def submit_login():
  email = request.form['email']
  contraseña = request.form['password']
  id_user = get_user_id(email)
  print(id_user)
  if id_user:
    if verify_password(id_user['id'], contraseña):
      my_session['logged'] = True
      my_session['id'] = id_user['id']
      my_session['usuario'] = id_user['usuario']
      return redirect(url_for('pagina_principal'))
    else:
      flash('Contraseña incorrecta', 'error')
      return redirect('/')
  else:
    flash('Usuario no registrado', 'error')
    return redirect('/')


# Ruta para redirigir a Flask usando el ID de la película
@app.route('/ver_pelicula/<uuid>')
def ver_pelicula(uuid):
  info = find_movie(uuid)
  comentarios = all_comments_by_movie(uuid)
  return render_template('info_pelicula.html',
                         info=info,
                         comentarios=comentarios)

@app.route('/insert_com/<movie_id>', methods=['POST'])
def insert_com(movie_id):    
    insert_comment(movie_id,request.form['comment'],my_session['usuario'])
    redirect(url_for('pagina_principal'))

if __name__ == '__main__':
  app.run(debug=True)
