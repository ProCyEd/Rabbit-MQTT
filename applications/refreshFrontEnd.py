from SQLite.StoreProcedures.getEquipment import getAllEquipment
from SQLite.StoreProcedures.getBoxes import getAllBoxes
import time
import publisher.IoTPublisher as pub
import json
import threading


def refresh(thread1):
    # threading.Lock(thread1)
    thread1.acquire()
    allEquipment = json.dumps(getAllEquipment())
    allboxes = json.dumps(getAllBoxes())
    print(allEquipment)
    print(allboxes)

    pub.publishCon(allEquipment)
    pub.publishCon(allboxes)
    print('published')
    thread1.release()
    time.sleep(30)
    refresh(thread1)
