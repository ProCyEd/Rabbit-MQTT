import sqlite3


def insertSubscribed(user_ip, session_token):
    conn = sqlite3.connect('IoT_Boxes.sqlite')

    c = conn.cursor()
    # Query using prepared statement
    query = """INSERT INTO subscribed (user_ip, session_token) VALUES (%s, %s)"""
    tuple = (user_ip, session_token)
    c.execute(query, tuple)

    conn.commit()
    conn.close()