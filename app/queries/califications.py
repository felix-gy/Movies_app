from Connection import *

def all_user_calification_by_movies(pelicula_id):
  with CassandraConnection() as session:
    result = session.execute(
        f"SELECT usuario,valor FROM calificaciones_peliculas WHERE pelicula_id= {pelicula_id};"
    )
  usuario = []
  if result:  
    for row in result:
      usuario.append({
        'usuario': row.usuario,
        'valor': row.valor
      })
  return usuario

def all_movie_califications_by_users(usuario):
  with CassandraConnection() as session:
    result = session.execute(
        f"SELECT pelicula_id,valor FROM calificaciones_usuarios WHERE usuario= {usuario};"
    )
  pelicula = []
  if result:  
    for row in result:
      pelicula.append({
        'usuario': row.usuario,
        'valor': row.valor
      })
  return pelicula

def promedio_by_movie(usuario):
  with CassandraConnection() as session:
    result = session.execute(
        f"SELECT pelicula_id,valor FROM calificaciones_usuarios WHERE usuario= {usuario};"
    )
  pelicula = []
  if result:  
    for row in result:
      pelicula.append({
        'usuario': row.usuario,
        'valor': row.valor
      })
  return pelicula
