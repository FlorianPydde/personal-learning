import sqlite3

connection = sqlite3.connect("database.db")


def find_user(username):
    with connection.cursor() as cur:
        cur.execute("""select username from USERS where name = '%s'""" % username)
        output = cur.fetchone()
    return output
