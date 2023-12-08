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
    return result