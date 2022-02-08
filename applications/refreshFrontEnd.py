from SQLite.StoreProcedures.getBoxes import getAllBoxes
import time
def refresh():
    while True:
        getAllBoxes()
        time.sleep(30)
