import sqlite3


def insertLog(user_ip, equipment_id):
    conn = sqlite3.connect('IoT_Boxes')

    c = conn.cursor()
    # Query using prepared statement
    query = """INSERT INTO log (user_ip, equipment_id) VALUES (%s, %s) """
    tuple = (user_ip, equipment_id)
    c.execute(query, tuple)
    conn.commit()
    conn.close()
    