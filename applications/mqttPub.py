import paho.mqtt.client as paho
import publisher.IoTPublisher as pub
import json
from SQLite.StoreProcedures.getBoxes import getAllBoxes
from SQLite.StoreProcedures.updateEquipment import updateState
from SQLite.StoreProcedures.insertBoxes import insertBoxes
from SQLite.StoreProcedures.insertEquipment import insertEquipment
from refreshFrontEnd import refresh
import threading
client2 = paho.Client('control2')


# this will send to the publisher to publisher to Rabbit
def on_message(client, userdata, message):

    print(message.payload.decode('utf-8'))
    m = json.loads(message.payload.decode('utf-8')) #decods the message into str then loads it into json
    method = m['method']
    if method == 'update_equipment_state':
        updateState(m['equipment_id'], m['equipment_state'])
        pub.publishCon(m)

    
    # pub.publishCon(getAllBoxes())



def connectCon():
    thread1 = threading.Lock()
    refresh(thread1)
    print('running mqttPub')
    thread1.acquire()
    broker = '199.244.104.202'
    client2.username_pw_set(username='dave', password='password')
    client2.connect(broker, 1883, 60)  # keeps the mqtt broker connection open for 60 seconds
    client2.subscribe('vmi/box/plug1/status')  # subscribes to the topic that will return the status of the broker
    client2.on_message = on_message
    client2.loop_forever()
    thread1.release()

if __name__ == "__main__":
    connectCon()
    