import psycopg2


def connector() -> psycopg2.extensions.connection:
    conn = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="jokerman218",
        database='library',
        port=2021)

    return conn

connector()