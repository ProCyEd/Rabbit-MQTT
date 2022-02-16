
import pika, os
import mqttCon as mqtt


url ='amqps://msdqunsz:8HfRRHR4k_1MnSrcSnL2dFadlDbYhsGJ@fish.rmq.cloudamqp.com/msdqunsz'
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()#start channel


def callback(ch, method, properties, body):

    print(f' [x] Received {str(body)}')
    if str(body).__contains__('True'):
        print(body)
        body = 'True'
        mqtt.connects(body)
    elif str(body).__contains__('False'):
        #print('[*]' + body)
        body = 'False'

        mqtt.connects(body)
    

channel.basic_consume(
    'frontendSend',
    callback,
    auto_ack=True
)

print(' [*]waiting for messages: ')
channel.start_consuming()


