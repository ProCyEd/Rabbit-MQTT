import paho.mqtt.client as mqtt
import consumer as con
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

    ret = con.callback
    #client.publish(ret.topic, ret.payload)
    print(ret+":"+client.publish("test", ret))
    pass


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("199.244.104.202", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
