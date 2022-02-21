import sqlite3


def insertBoxes(box_id, box_name):
    conn = sqlite3.connect('IoT_Boxes')

    c = conn.cursor()
    # Query using prepared statement
    query = "INSERT INTO boxes (box_id, box_name) VALUES (%s, %s)"
    tuple = (box_id, box_name)
    c.execute(query, tuple)
    conn.commit()
    conn.close()



