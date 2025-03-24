import psycopg2

connection_info = {
    "host": 'localhost',
    "port": 5432,
    "user": 'postgres',
    "password": 'coderslab',
    "database": 'postgres',
}

def execute_sql(query, name = None, *variables):
    if name is not None:
        connection_info['database'] = name
    connection = psycopg2.connect(**connection_info)
    connection.autocommit = True
    cursor = connection.cursor()
    cursor.execute(query, variables)
    try:
        return cursor.fetchall()
    except psycopg2.ProgrammingError:
        return None
    finally:
        cursor.close()
