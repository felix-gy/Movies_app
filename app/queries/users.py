from Connection import *
import uuid
import bcrypt


def insert_user(name, email, password):
  with CassandraConnection() as session:
    id_user = uuid.uuid4()
    # Encriptaciòn
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    hashed_password_str = hashed_password.decode('utf-8')
    # session.execute(f"""
    #     INSERT INTO usuarios (id, nombre, gmail, password)
    #     VALUES ('{id_user}', '{name}', '{email}','{hashed_password}')
    # """)
    session.execute(
        f"INSERT INTO usuariosp (id, usuario, gmail, password) VALUES ({id_user}, '{name}', '{email}', '{hashed_password_str}');"
    )


def get_user_id(email):
  with CassandraConnection() as session:
    result = session.execute(
        f"SELECT id, usuario FROM usuariosp WHERE gmail = '{email}'ALLOW FILTERING;"
    )
  user = {}
  if result:
    for row in result:
      user['id'] = row.id
      user['usuario'] = row.usuario
  else:
    return None
  return user


def verify_password(id, password):

  with CassandraConnection() as session:
    result = session.execute(
        f"SELECT password FROM usuariosp WHERE id = {id} LIMIT 1 ALLOW FILTERING;"
    )
  if result:
    for row in result:
      hashed_password = row.password
  else:
    return False
  if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
    return True
  else:
    return False
