import sqlite3


def insertSubscribed(user_ip, session_token):
    conn = sqlite3.connect('IoT_Boxes.db')

    c = conn.cursor()

    query = """INSERT INTO subscribed (user_ip, session_token) VALUES (%s, %s)"""
    tuple = (user_ip, session_token)
    c.execute(query, tuple)

    #items = c.fetchall()
    conn.commit()
    conn.close()
    #return items