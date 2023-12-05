from Connection import *

def test_1():
    con = connectionDB()
    # Preparar la consulta
    consulta = "SELECT * FROM peliculas"
    
    # Ejecutar la consulta
    resultado = con[1].execute(consulta)

    datos_peliculas = []
    for fila in resultado:
        datos_pelicula = {
            'id': fila.id,
            'titulo': fila.titulo,
            'descripcion': fila.descripcion,
            'generos': fila.generos,
            'fecha_estreno': fila.fecha_estreno,
            'imagen': fila.imagen
        }
        datos_peliculas.append(datos_pelicula)

    # Cerrar la conexión
    con[0].shutdown()
    return str(datos_peliculas)