import logging
import paho.mqtt.client as paho
import time
import json
import consumer

client1= paho.Client('control1')


def on_publish(client, userdata, result):
    print('data published \n')
    pass


def on_log(client, userdata, level, buf):
        print(f'log con: {buf}')
        print(f'log data: {userdata}')


def connects(body):
   
    
    client1.on_publish = on_publish
    client1.on_log = on_log
    client1.connect(broker,1883,60)#keeps the mqtt broker connection open for 60 seconds
    ret=client1.publish("test", body)
    time.sleep(2)


