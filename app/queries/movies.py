from Connection import *

from Connection import *
import uuid

# from conDB import *


def all_movies():
  with CassandraConnection() as session:
    query = "SELECT id, titulo FROM peliculas"
    rows = session.execute(query)
    peliculas = []
    for row in rows:
      peliculas.append({
          'id': row.id,
          'titulo': row.titulo,
      })
  return peliculas


def find_movie(uuid):
  with CassandraConnection() as session:
    result = session.execute(f"SELECT * FROM peliculas WHERE id = {uuid}")
  peliculas = []
  for row in result:
    peliculas.append({
        'id': row.id,
        'titulo': row.titulo,
        'fecha_estreno': row.fecha_estreno,
        'generos': row.generos,
        'descripcion': row.descripcion,
    })
  return peliculas


def movie_rating(movie_id):
    with CassandraConnection() as session:
        result = session.execute(f"SELECT * FROM promedios WHERE pelicula_id = {movie_id};")
    return result


