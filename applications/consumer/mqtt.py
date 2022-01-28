import logging
import paho.mqtt.client as paho
import time


client1= paho.Client('control1')
def on_disconnect(client, userdata, rc=0):
    logging.debug("Disconnected result code: {0}", str(rc))
    client1.loop_stop()
    

def connect(body):
    def on_publish(client, userdata, result):
        print('data published \n')
        pass

    def on_log(client, userdata, level, buf):
        print(f'log: {buf}')

   
    
        

    broker = '199.244.104.202'
    # client1= paho.Client('control1')
    client1.on_publish = on_publish
    client1.on_log = on_log
    client1.connect(broker,1883,60)#keeps the mqtt broker connection open for 60 seconds
    client1.loop_start()
    ret=client1.publish("test", body)
    time.sleep(4)

# if client1.on_unsubscribe():
#     on_disconnect()