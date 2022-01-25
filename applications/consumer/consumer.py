import pika, os
import paho.mqtt.client as paho
import mqtt

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

    print(' [x] Received '+ str(body))
    if body == '"on"':
        body = 'on'
    else:
        body = 'off'
    # client1= paho.Client('control1')
    # client1.on_publish = on_publish
    # client1.connect(broker)
    #ret=client1.publish("test", body)
    ret=mqtt.client1.publish("test", body)
    connection.close()
    

# channel.basic_consume(
#     'frontendSend',
#     callback,
#     auto_ack=True
# )

print(' [*]waiting for messages: ')
channel.start_consuming()
connection.close()
