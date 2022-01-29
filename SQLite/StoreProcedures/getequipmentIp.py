import sqlite3

def getEquipId(equipment_id, box_sid):
    conn = sqlite3.connect('IoT_Boxes.db')

    c = conn.cursor()

    c.execute(""" 
        SELECT * FROM equipment WHERE equipment.equipment_id = equipment_id AND equipment.box_sid = box_sid
    """)

    items = c.fetchall()
    conn.commit()
    conn.close()
    return items