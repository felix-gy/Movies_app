from Connection import *
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

# def movies_id(uuid):
#     con = connectionDB()
#     query_pelicula = "SELECT id, titulo, descripcion, generos, fecha_estreno, imagen FROM peliculas WHERE id = %s"
#     pelicula_result = con[0].execute(query_pelicula, (uuid,))

#     return pelicula_result  # Ass

