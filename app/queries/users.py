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
        session.execute(f"INSERT INTO usuarios (id, usuario, gmail, password) VALUES ({id_user}, '{name}', '{email}', '{hashed_password_str}');")    

def get_user_id(email):
    with CassandraConnection() as session:
        result = session.execute(f"SELECT id FROM usuarios WHERE gmail = '{email}' ALLOW FILTERING;")    
    if result:
        for row in result:
            return row.id
    else:
        return None
def verify_password(id, password):

    print(password)
    with CassandraConnection() as session:
        result = session.execute(f"SELECT password FROM usuarios WHERE id = {id} LIMIT 1;")  
    if result:
        for row in result:
            hashed_password = row.password

    if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
        return True
    else:
        return False

