from SQLite.StoreProcedures.getBoxes import getAllBoxes
import time
import publisher.publisher as pub
#def refresh():
while True:
        print(getAllBoxes())
        #pub.publishCon(getAllBoxes())
        time.sleep(30)
