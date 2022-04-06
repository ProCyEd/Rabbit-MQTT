from SQLite.StoreProcedures.getEquipment import getAllEquipment
import time
import publisher.publisher as pub
import json
import threading
def refresh(thread1):
    
        #threading.Lock(thread1)
        thread1.acquire()
        allEquipment = json.dump(getAllEquipment())
        print(allEquipment)
        pub.publishCon(allEquipment)
        print('published')
        thread1.release()
        time.sleep(30)
        refresh(thread1)
