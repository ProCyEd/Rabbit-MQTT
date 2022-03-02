import paho.mqtt.client as paho
import publisher.publisher as pub
import json
from SQLite.StoreProcedures.getBoxes import getAllBoxes
from SQLite.StoreProcedures.updateEquipment import updateState

client2 = paho.Client('control2')


# this will send to the publisher to publisher to Rabbit
def on_message(client, userdata, message):
    # print("received message: ", str(message.payload.decode('utf-8')))
    # msg = str(message.payload.decode('utf-8'))

    m = json.loads(message)
    method = m['method']
    if method == 'update_equipment_state':
        updateState(m['equipment_id'], m['box_id'],
                    m['equipment_state'])
    # pub.publishCon(getAllBoxes())
    # m = json.JSONDecoder.decode(message)
    # print(msg)
    # print(m_in)
    # print(m)


def connectCon():
    print('running mqttPub')
    broker = '199.244.104.202'
    client2.username_pw_set(username='dave', password='password')
    client2.connect(broker, 1883, 60)  # keeps the mqtt broker connection open for 60 seconds
    client2.subscribe('vmi/box1/plug1/status')  # subscribes to the topic that will return the status of the broker
    client2.on_message = on_message
    client2.loop_forever()


if __name__ == "__main__":
    connectCon()
