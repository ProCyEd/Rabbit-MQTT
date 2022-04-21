import sqlite3


def insertBoxes(box_id, box_name, location):
    conn = sqlite3.connect('IoT_Boxes.sqlite')

    c = conn.cursor()
    # Query using prepared statement
    query = "INSERT INTO boxes (box_id, box_name, location) VALUES (?, ?, ?)"
    tuple = (box_id, box_name, location)
    c.execute(query, tuple)
    conn.commit()
    conn.close()



