import pika, os
import mqttCon as mqtt

url = 'amqps://msdqunsz:8HfRRHR4k_1MnSrcSnL2dFadlDbYhsGJ@fish.rmq.cloudamqp.com/msdqunsz'
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()  # start channel


# this callback method is whats being called when you consume from rabbit
def callback(ch, method, properties, body):
    print(f' [x] Received {body}')
    if str(body).__contains__('True'):
        print(body)
        body = 'True'
        mqtt.connects(body)  # calls the connects method in mqtt^
    elif str(body).__contains__('False'):
        body = 'False'
        mqtt.connects(body)


# this will consume from the frontendSend Queue in Rabbit
channel.basic_consume(
    'frontendSend',
    callback,
    auto_ack=True
)

print(' [*]waiting for messages: ')
channel.start_consuming()
