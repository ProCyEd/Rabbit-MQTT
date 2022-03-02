import sqlite3


def updateState(equipment_id, box_id, equipment_state):
    conn = sqlite3.connect('IoT_Boxes')

    c = conn.cursor()
    # Query using prepared statement
    query = """UPDATE equipment SET equipment_state = %s WHERE equipment_id = %s AND box_id = %s """
    tuple = (equipment_state, equipment_id, box_id)
    c.execute(query, tuple)
    conn.commit()
    conn.close()
