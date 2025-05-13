import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="forumdb",
        user="postgres",
        password="1325",
        host="localhost",
        port="5432",
        options="-c client_encoding=UTF8"
    )
