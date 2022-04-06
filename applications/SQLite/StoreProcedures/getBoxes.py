import sqlite3


def getAllBoxes():
    conn = sqlite3.connect('IoT_Boxes.sqlite')  # connects to the db, if it doesnt exist it will create one, but it wont
                                         # because the only reason to call this is if you have this db.

    c = conn.cursor()

    c.execute("SELECT * FROM boxes")  # gets all the boxes from boxes
    items = c.fetchall()  # puts all the data into a var

    conn.commit()
    conn.close()
    return items



