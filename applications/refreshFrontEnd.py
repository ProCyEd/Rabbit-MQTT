from SQLite.StoreProcedures.getBoxes import getAllBoxes
import time
import publisher.publisher as pub
import json
# def refresh():
while True:

    l = json.dump(getAllBoxes())
    print(l)
    # pub.publishCon(getAllBoxes())
    time.sleep(30)
