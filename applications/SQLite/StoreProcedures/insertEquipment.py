import sqlite3


def insertEquipment(equipment_id, box_id, equipment_name, equipment_state, equipment_ip):
    conn = sqlite3.connect('IoT_Boxes')

    c = conn.cursor()
    # Query using prepared statement
    query = """INSERT INTO boxes (equipment_id, box_id, equipment_name, equipment_state, equipment_ip)) 
                VALUES (%s, %s, %s,%s,%s)"""
    tuple = (equipment_id, box_id, equipment_name, equipment_state, equipment_ip)
    c.execute(query, tuple)
    conn.commit()
    conn.close()
