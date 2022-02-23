import sqlite3


def insertBoxes(templateName, templateFile):
    conn = sqlite3.connect('File_Templates')
    read = ''
    with open(templateFile) as f:
        read = f.read()
    c = conn.cursor()
    # Query using prepared statement
    query = "INSERT INTO templates (template_name, template_data) VALUES (%s, %s)"
    tuple = (templateName, read)
    c.execute(query, tuple)
    conn.commit()
    conn.close()