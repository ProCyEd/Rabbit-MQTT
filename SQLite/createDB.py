import sqlite3

conn = sqlite3.connect('IoT_Boxes.db')

c = conn.cursor()

c.execute("""
    CREATE TABLE boxes(
        box_id INTEGER PRIMARY KEY,
        box_name NOT NULL UNIQUE
    )
""")

c.execute(""" 
    CREATE TABLE equipment(
        equipment_id INTEGER PRIMARY KEY,
        box_sid INTEGER,
        equipment_name TEXT,
        equipment_state INTEGER,
        equipment_ip TEXT,
        FOREIGN KEY(box_sid) REFERENCES boxes(sid)
    )
""")

c.execute(""" 
    CREATE TABLE log(
        user_ip TEXT PRIMARY KEY,
        equipment_id INTEGER,
        equipment_state = {SELECT equipment_state FROM equipment WHERE equipment.equipment_id = equipment_id},
        FOREIGN KEY(equipment_id) REFERENCES equipment(equipment_id),
        
    )
""")
c.execute(""" 

    CREATE TABLE token(
        session_token TEXT PRIMARY KEY,
        box_id INTEGER,
        FOREIGN KEY(box_id) REFERENCES boxes(box_id)
    )
""")

c.execute(""" 

    CREATE TABLE subscribed(
        user_ip TEXT PRIMARY KEY,
        session_token TEXT,
        FOREIGN KEY(session_token) REFERENCES token(session_token)
    )
""")
