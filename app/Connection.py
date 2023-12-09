from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import json

class CassandraConnection:
  def __init__(self):

    self.keyspace = 'pelicula'

    cloud_config= {
      'secure_connect_bundle': 'app/secure-connect-pelicula-foro.zip'
    }
    with open("app/pelicula_foro-token.json") as f:
      secrets = json.load(f)

    CLIENT_ID = secrets["clientId"]
    CLIENT_SECRET = secrets["secret"]
    auth_provider = PlainTextAuthProvider(CLIENT_ID, CLIENT_SECRET)
    self.cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
    self.session = self.cluster.connect(self.keyspace)

  def __enter__(self):
    return self.session

  def __exit__(self, exc_type, exc_val, exc_tb):
    self.session.shutdown()
    self.cluster.shutdown()

  