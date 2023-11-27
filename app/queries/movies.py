from local_conDB import *
# from conDB import *



def all_movies():
    con = connectionDB()
    query = "SELECT id, titulo, imagen FROM peliculas"
    result = con[0].execute(query)

    #cerrar conexcion 
    con[1].shutdown()
    
    return result
