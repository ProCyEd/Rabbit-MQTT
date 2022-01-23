import pika, os
import mqttPublish as paho
#from paho import on_message



url ='amqps://msdqunsz:8HfRRHR4k_1MnSrcSnL2dFadlDbYhsGJ@fish.rmq.cloudamqp.com/msdqunsz'#'amqp://guest:guest@localhost:5672/')#'amqps://msdqunsz:8HfRRHR4k_1MnSrcSnL2dFadlDbYhsGJ@fish.rmq.cloudamqp.com/msdqunsz')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()#start channel
#channel.queue_declare(queue='frontendSend')

def callback(ch, method, properties, body):
    print(' [x] Received '+ str(body))
    # paho.on_message(paho.client, str(body))
    #paho.client.publish(str(body))
    

channel.basic_consume(
    'frontendSend',
    callback,
    auto_ack=True
)

print(' [*]waiting for messages: ')
channel.start_consuming()



connection.close()
