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
    movie_details = None
    with CassandraConnection() as session:

        result = session.execute(f"SELECT * FROM peliculas WHERE id = {uuid}")
        # prepared = session.prepare('SELECT * FROM peliculas WHERE id = ?;')
        # #query = "SELECT * FROM peliculas WHERE id = %s;"
        # obj = uuid.UUID(uuid)
        # bound = prepared.bind([obj])
        # print("aaa")
        # print(uuid)
        # rows = session.execute(bound)
        for row in result:
             movie_details = row
             break
    return result