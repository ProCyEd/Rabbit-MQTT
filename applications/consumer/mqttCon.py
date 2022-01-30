import logging
import paho.mqtt.client as paho
import time
import publisher.publisher as pub


client2= paho.Client('control2')
def on_disconnect(client, userdata, rc=0):
    time.sleep(1)
    logging.debug("Disconnected result code: {0}", str(rc))
    client2.loop_stop()

def on_message(client, userdata, message):
    print("received message: ", str(message.payload.decode("utf-8")))
    pub.publishCon(message)

def connectCon():
   

    broker = '199.244.104.202'
    # client1= paho.Client('control1')
    
   
    client2.connect(broker,1883,60)#keeps the mqtt broker connection open for 60 seconds
    client2.loop_start()
    ret=client2.on_message
    time.sleep(4)

# if client1.on_unsubscribe():
#     on_disconnect()