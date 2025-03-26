import psycopg2
from sql_utilis import execute_sql
#
# sql = "CREATE DATABASE workshop;"
# sql1 = """CREATE TABLE users(
#             id serial PRIMARY KEY NOT NULL,
#             login varchar(30),
#             password varchar(30),
#             confirm_password varchar(30));"""
#
# #execute_sql(sql)
# execute_sql(sql1, "workshop")

# sql2 = """CREATE TABLE messages(
#             id SERIAL PRIMARY KEY,
#             from_id INTEGER,
#             to_id INTEGER,
#             creation_date date,
#             text TEXT);"""
#
# execute_sql(sql2, 'workshop')

sql3 = """ALTER TABLE messages
ADD CONSTRAINT fk_messages_from_user
FOREIGN KEY (from_id) REFERENCES users(id),
ADD CONSTRAINT fk_messages_to_user
FOREIGN KEY (to_id) REFERENCES users(id);"""

execute_sql(sql3, 'workshop')