
import pika, os
import mqttPub as mqtt


url ='amqps://msdqunsz:8HfRRHR4k_1MnSrcSnL2dFadlDbYhsGJ@fish.rmq.cloudamqp.com/msdqunsz'
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()#start channel



def callback(ch, method, properties, body):

    print(f' [x] Received {body}')
    if str(body) == "b'on'":
        body = 'on'
        mqtt.connects(body)
    elif str(body) == "b'off'":
        body = 'off'
        mqtt.connects(body)
    
    
    

channel.basic_consume(
    'frontendSend',
    callback,
    auto_ack=True
)

print(' [*]waiting for messages: ')
channel.start_consuming()


