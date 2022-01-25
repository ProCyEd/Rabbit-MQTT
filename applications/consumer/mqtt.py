import paho.mqtt.client as paho

def on_publish(client, userdata, result):
    print('data published \n')
    pass


broker = '199.244.104.202'
client1= paho.Client('control1')
client1.on_publish = on_publish
client1.connect(broker)