import sqlite3


def updateState(id, state):
    conn = sqlite3.connect('IoT_Boxes')
    c = conn.cursor()
    # Query using prepared statement
    query = """UPDATE equipment SET equipment_state = ? WHERE equipment_id = ? """
    t = (state, id)
    c.execute(query, t)
    conn.commit()
    conn.close()
