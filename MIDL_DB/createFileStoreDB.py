import sqlite3

conn = sqlite3.connect('File_Templates')

c = conn.cursor()

command1 = """
    CREATE TABLE IF NOT EXISTS templates(
        template_id INTEGER PRIMARY KEY,
        template_name TEXT NOT NULL UNIQUE,
        template_data TEXT 
    )
"""
c.execute(command1)

conn.commit()
conn.close()
