import sqlite3


def removeToken(session_token):
    conn = sqlite3.connect('IoT_Boxes')

    c = conn.cursor()

    query = """DELETE FROM token WHERE token.session_token = %s"""
    tuple = (session_token)
    c.execute(query, tuple)

    #items = c.fetchall()
    conn.commit()
    conn.close()
    