import sqlite3

def getAllBoxes():
    conn = sqlite3.connect('IoT_Boxes.db')

    c = conn.cursor()

    c.execute("SELECT * FROM  boxes")

    items = c.fetchall()

    conn.commit()
    conn.close()
    return items