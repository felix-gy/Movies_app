
from Connection import *


def all_comments_by_movie(movie_id):
  with CassandraConnection() as session:
    result = session.execute(
        f"SELECT usuario, texto,fecha_creacion FROM comentarios_peliculasp WHERE pelicula_id = {movie_id};"
    )
  comments = []
  if result:
    for row in result:
      timestamp_value = row.fecha_creacion
      formatted_date_time = timestamp_value.strftime('%Y-%m-%d %H:%M')
      comments.append({
          'usuario': row.usuario,
          'texto': row.texto,
          'fecha_creacion': formatted_date_time,
      })
  return comments


def all_comments_by_user(usuario_id):
  with CassandraConnection() as session:
    result = session.execute(
        f"SELECT pelicula_id, texto,fecha_creacion FROM comentarios_usuariosp WHERE usuario = {usuario_id};"
    )
  comments = []
  if result:  
    for row in result:
      timestamp_value = row.fecha_creacion
      formatted_date_time = timestamp_value.strftime('%Y-%m-%d %H:%M')
      comments.append({
          'pelicula_id': row.pelicula_id,
          'texto': row.texto,
          'fecha_creacion': formatted_date_time,
      })
  return comments

def insert_comment(movie_id,text,usuario):
  with CassandraConnection() as session:
      result = session.execute(
          f"INSERT INTO comentarios_peliculasp (pelicula_id, usuario, texto,fecha_creacion) VALUES ({movie_id},'{usuario}','{text}',dateof(now()));"
      )