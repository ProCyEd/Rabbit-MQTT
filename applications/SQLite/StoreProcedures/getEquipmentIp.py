import sqlite3


def getEquipIP(equipment_id, box_id):
    conn = sqlite3.connect('IoT_Boxes.db')

    c = conn.cursor()

    # Query using prepared statement
    query = """SELECT equipment_ip FROM equipment WHERE equipment.equipment_id = %s AND equipment.box_sid = %s"""
    t = (equipment_id, box_id)
    c.execute(query, t)

    items = c.fetchall()
    conn.commit()
    conn.close()
    return items