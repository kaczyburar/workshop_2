import psycopg2
from sql_utilis import execute_sql

sql = "CREATE DATABASE workshop;"
sql1 = """CREATE TABLE users(
            id serial PRIMARY KEY NOT NULL,
            login varchar(30),
            password varchar(30),
            confirm_password varchar(30));"""

#execute_sql(sql)
execute_sql(sql1, "workshop")