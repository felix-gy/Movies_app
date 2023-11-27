from cassandra.cluster import Cluster
# Conectarse al clúster de Cassandra
def connectionDB():
    cluster = Cluster(['localhost'])
    session = cluster.connect()
    # Crear o seleccionar un keyspace
    session.execute("CREATE KEYSPACE IF NOT EXISTS movies_app WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor': 1}")
    session.set_keyspace('movies_app')
    if session:
        return [session,cluster]
    else:
        print("error de conexion")


