import paho.mqtt.client as paho
import time
import json
client1 = paho.Client('control1')


# def on_publish(client, userdata, result):
#     print('data published \n')
#     pass


# this will log all connects to the broker as well as data being sent
def on_log(client, userdata, level, buf):
    print(f'log con: {buf}')
    # print(logging.)
    print(f'log data: {userdata}')


# this will connect to the broker and publish to the broker
def connects(body):
    client1.username_pw_set(username='dave', password='password')
    broker = '199.244.104.202'
    # client1.on_publish = on_publish
    client1.on_log = on_log

    client1.connect(broker, 1883, 60)  # keeps the mqtt broker connection open for 60 seconds
    client1.publish("vmi/box1/plug1", body) # publish to a specific tag and your payload

    time.sleep(2)
