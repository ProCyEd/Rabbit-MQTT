import sqlite3


def insertLog(user_ip, equipment_id):
    conn = sqlite3.connect('IoT_Boxes')

    c = conn.cursor()

    query = """INSERT INTO log (user_ip, equipment_id) VALUES (%s, %s) """
    tuple = (user_ip, equipment_id)
    c.execute(query, tuple)

    #items = c.fetchall()
    conn.commit()
    conn.close()
    