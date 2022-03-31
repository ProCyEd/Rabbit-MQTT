import sqlite3


def getEquipType(equipment_id, box_id):
    conn = sqlite3.connect('IoT_Boxes.db')

    c = conn.cursor()

    # Query using prepared statement
    query = """SELECT equipment_name FROM equipment WHERE equipment.equipment_id = ? AND equipment.box_sid = ?"""
    t = (equipment_id, box_id)
    c.execute(query, t)

    items = c.fetchall()
    conn.commit()
    conn.close()
    return items