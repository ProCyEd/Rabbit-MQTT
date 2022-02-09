from SQLite.StoreProcedures.getBoxes import getAllBoxes
import time
import publisher.publisher as pub
def refresh():
    while True:
        
        pub.publishCon(getAllBoxes())
        time.sleep(30)
