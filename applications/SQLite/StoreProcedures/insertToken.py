import sqlite3


def insertToken(session_token, box_id):
    conn = sqlite3.connect('IoT_Boxes')

    c = conn.cursor()

    query = """INSERT INTO token (session_token, box_id) values (%s, %s)"""
    tuple = (session_token, box_id)
    c.execute(query, tuple)

    #items = c.fetchall()
    conn.commit()
    conn.close()
    