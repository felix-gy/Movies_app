from flask import Flask, render_template, request, redirect,url_for
from queries.movies import *
from queries.users import *

app = Flask(__name__)

my_session = {'logged':False}

@app.route('/')
def index():
    peliculas = all_movies()
    return render_template('BDII_index.html', peliculas=peliculas)

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/submit_register', methods=['POST'])
def submit_register():
    nombre = request.form['nombre']
    email = request.form['email']
    contraseña = request.form['password']
    insert_user(nombre,email,contraseña)
    return 'Formulario enviado correctamente - register '

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/submit_login', methods=['POST'])
def submit_login():
    email = request.form['email']
    contraseña = request.form['password']
    id_user = get_user_id(email)
    if id_user:
        if verify_password(id_user, contraseña):
            my_session['logged'] = True
            my_session['id'] = id_user
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))

# Ruta para redirigir a Flask usando el ID de la película
@app.route('/ver_pelicula/<uuid>')
def ver_pelicula(uuid):    
    info = find_movie(uuid)
    return render_template('info_pelicula.html', info=info)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)