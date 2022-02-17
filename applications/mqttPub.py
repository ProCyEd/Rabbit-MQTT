import paho.mqtt.client as paho
import publisher.publisher as pub
import json

client2 = paho.Client('control2')


def on_message(client, userdata, message):
    print("received message: ", str(message.payload.decode('utf-8')))
    msg = str(message.payload.decode('utf-8'))
    pub.publishCon(msg)


def connectCon():
    print('running mqttPub')
    broker = '199.244.104.202'
    # client1= paho.Client('control1')
    client2.username_pw_set(username='dave', password='password')
    client2.connect(broker, 1883, 60)  # keeps the mqtt broker connection open for 60 seconds
    client2.subscribe('vmi/box1/plug1/status')
    client2.on_message = on_message
    client2.loop_forever()


if __name__ == "__main__":
    connectCon()
