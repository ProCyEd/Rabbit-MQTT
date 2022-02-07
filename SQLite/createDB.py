import sqlite3

conn = sqlite3.connect('IoT_Boxes.db')

c = conn.cursor()

c.execute("""
    CREATE TABLE boxes(
        sid INTEGER PRIMARY KEY,
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

    )
""")
