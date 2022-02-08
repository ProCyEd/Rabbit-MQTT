
from concurrent.futures import thread

import paho.mqtt.client as paho
import time
import publisher.publisher as pub



client2= paho.Client('control2')



def on_message(client, userdata, message):
    print("received message: ", str(message.payload.decode("utf-8")))
    pub.publishCon(message)


def connectCon():
   
    print('running mqttPub')
    
    
    broker = '199.244.104.202'
    # client1= paho.Client('control1')
    client2.on_message = on_message
    client2.connect(broker,1883,60)#keeps the mqtt broker connection open for 60 seconds
    
    client2.loop_forever()
    
    #time.sleep(3)
    
    
    
    # ret=client2.on_message


if __name__ =="__main__":
    connectCon()