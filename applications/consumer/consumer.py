from ast import Break
import pika, os
# import paho.mqtt.client as paho
import mqttPub as mqtt

url ='amqps://msdqunsz:8HfRRHR4k_1MnSrcSnL2dFadlDbYhsGJ@fish.rmq.cloudamqp.com/msdqunsz'#'amqp://guest:guest@localhost:5672/')#'amqps://msdqunsz:8HfRRHR4k_1MnSrcSnL2dFadlDbYhsGJ@fish.rmq.cloudamqp.com/msdqunsz')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()#start channel
#channel.queue_declare(queue='frontendSend')

# broker = '199.244.104.202'

# def on_publish(client, userdata, result):
#     print('data published \n')
#     pass



def callback(ch, method, properties, body):

    print(f' [x] Received {body}')
    if str(body) == "b'on'":
        print("hehe")
        body = 'on'
        mqtt.connect(body)
    elif str(body) == "b'off'":
        print('heler')
        body = 'off'
        mqtt.connect(body)
    elif str(body) == "b'disconnect'":
        print('unsub')
        mqtt.client1.on_disconnect = mqtt.on_disconnect
        
    # mqtt.connect(body)
    # client1= paho.Client('control1')
    # client1.on_publish = on_publish
    # client1.connect(broker)
    #ret=client1.publish("test", body)
    
    # ret=client1.publish("test", body)
    
    

channel.basic_consume(
    'frontendSend',
    callback,
    auto_ack=True
)

print(' [*]waiting for messages: ')
channel.start_consuming()
connection.close()
