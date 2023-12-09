from flask import Flask, render_template, request, redirect,url_for
from queries.movies import *

app = Flask(__name__)


@app.route('/')
def index():
    peliculas = all_movies()
    return render_template('BDII_index.html', peliculas=peliculas)

# Ruta para redirigir a Flask usando el ID de la película
@app.route('/ver_pelicula/<uuid>')
def ver_pelicula(uuid):    
    info = find_movie(uuid)
    return render_template('info_pelicula.html', info=info)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080,debug=True)