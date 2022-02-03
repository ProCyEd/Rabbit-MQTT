import sqlite3

def getEquipId(equipment_id, box_sid):
    conn = sqlite3.connect('IoT_Boxes.db')

    c = conn.cursor()

   
    query = """SELECT 1 FROM equipment WHERE equipment.equipment_id = %s AND equipment.box_sid = %s"""
    tuple = (equipment_id, box_sid)
    c.execute(query, tuple)


    items = c.fetchall()
    conn.commit()
    conn.close()
    return items