from flask import Flask, render_template, request, redirect,url_for
app = Flask(__name__)


from queries.test import *


@app.route('/')
def index():
    return "test: "+ test_1()




if __name__ == '__main__':
    app.run(debug=True)


















# docker run --name test-cassandra-v2 -p 9042:9042  cassandra:latest
# docker exec -it test-cassandra-v2 bash
# pip3 install cassandra-driver

# from cassandra.cluster import Cluster

# cluster = Cluster(['0.0.0.0'], port=9042)
# session = cluster.connect()
# KEYSPACE = "playersessionservicekey"

# session.execute("""
#         CREATE KEYSPACE IF NOT EXISTS %s
#         WITH replication = { 'class': 'SimpleStrategy', 'replication_factor': '2' }
#         """ % KEYSPACE)

# session.execute("use playersessionservicekey")

# session.set_keyspace(KEYSPACE)


# session.execute("""
#         CREATE TABLE IF NOT EXISTS Playersessionservicetable (
#             country text,
#             event text,
#             player_id text,
#             session_id text,
#             ts timestamp,
#             PRIMARY KEY (player_id,session_id,ts)
#         )
#         """)

# print("Setup is done...")

#! Writing data into cassandra
# session.execute("INSERT INTO employee_details (id, age, city, name) VALUES (99,20,'Chicago','Max');")
# session.execute_async("INSERT INTO employee_details (id, age, city, name) VALUES (400,25,'Seattle','Bob');")