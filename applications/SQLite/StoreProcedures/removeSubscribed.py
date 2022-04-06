import sqlite3


def getEquipId(session_token):
    conn = sqlite3.connect('IoT_Boxes.sqlite')

    c = conn.cursor()
    # Query using prepared statement
    query = """DELETE FROM subscribed WHERE subscribed.session_token = %s"""
    tuple = session_token
    c.execute(query, tuple)

    conn.commit()
    conn.close()