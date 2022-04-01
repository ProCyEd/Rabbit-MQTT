from SQLite.StoreProcedures.getEquipment import getAllEquipment
import time
import publisher.publisher as pub
import json
def refresh():
    while True:

        allEquipment = json.dump(getAllEquipment())
        pub.publishCon(allEquipment)
        time.sleep(30)
