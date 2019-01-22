from pprint import pprint
import psycopg2
import psycopg2.extras
from dbconnect import connect

conn = connect()

def create_users():
    """Creates the users Table for registration of New users in my Flask App"""
    sql_create = """CREATE TABLE IF NOT EXISTS dev_test.tbl_users(id serial PRIMARY KEY, created_registered_at timestamptz not null default now(), name varchar(50), email varchar(100), username varchar(50), password varchar(100)  )"""
    cur  = None
    message = None
    try:
        cur = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
        pprint(cur)
        if cur:
            cur.execute(sql_create)
            conn.commit()
            message = "Table created Successfully"
            pprint(message)

    except Exception as e:
        pprint(e),pprint(type(e))
        message = "General Error"
        pprint(message)

    finally:
        if conn is not None:
            conn.close()
        return message
