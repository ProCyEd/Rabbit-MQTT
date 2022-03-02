import sqlite3


def extractTemplate(template_id):
    conn = sqlite3.connect('File_Templates')

    c = conn.cursor()

    # Query using prepared statement
    query = """SELECT template_data FROM templates WHERE template_id = %s"""
    t = template_id
    c.execute(query, t)

    items = c.fetchall()
    conn.commit()
    conn.close()
    return items