import sqlite3

conn = sqlite3.connect('../applications/IoT_Boxes')

c = conn.cursor()

command1 = """
    CREATE TABLE IF NOT EXISTS boxes(
        box_id INTEGER PRIMARY KEY,
        box_name NOT NULL UNIQUE
    )
"""
c.execute(command1)

command2 = """ 
    CREATE TABLE IF NOT EXISTS equipment(
        equipment_id INTEGER PRIMARY KEY,
        box_id INTEGER,
        equipment_name TEXT,
        equipment_state INTEGER,
        equipment_ip TEXT,
        FOREIGN KEY(box_id) REFERENCES boxes(box_id)
    )
"""
c.execute(command2)

command3 = """ 
    CREATE TABLE IF NOT EXISTS log(
        user_ip TEXT PRIMARY KEY,
        equipment_id INTEGER,
        equipment_state INTEGER,
        FOREIGN KEY(equipment_id) REFERENCES equipment(equipment_id)
        
    )
"""
c.execute(command3)

command4 = """ CREATE TABLE IF NOT EXISTS token(
        session_token TEXT PRIMARY KEY,
        box_id INTEGER,
        FOREIGN KEY(box_id) REFERENCES boxes(box_id)
    )
"""
c.execute(command4)

command5 = """ 

    CREATE TABLE IF NOT EXISTS subscribed(
        user_ip TEXT PRIMARY KEY,
        session_token TEXT,
        FOREIGN KEY(session_token) REFERENCES token(session_token)
    )
"""
c.execute(command5)

conn.commit()
conn.close()
