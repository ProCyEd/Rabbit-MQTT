import pika, os
import mqttCon as mqtt
import SQLite.StoreProcedures.getEquipmentIp as ip
import SQLite.StoreProcedures.getEquipmentType as eT

import json

url = 'amqps://msdqunsz:8HfRRHR4k_1MnSrcSnL2dFadlDbYhsGJ@fish.rmq.cloudamqp.com/msdqunsz'
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()  # start channel


# this callback method is whats being called when you consume from rabbit
def callback(ch, method, properties, body):
    recivedMsg = json.dumps(body)

    topic = recivedMsg['topic']
    command = recivedMsg['command']

    print(f' [x] Received {recivedMsg}')

    message = {
        'ip': ip.getEquipIP(recivedMsg['equipment_type'], recivedMsg['box_id']),
        'equipment_type': eT.getEquipType(recivedMsg['equipment_type'], recivedMsg['box_id']),
        'equipment_id': recivedMsg['equipment_id'],
        'command': command,
        'topic': topic
    }
    mqtt.connects(message)

    # if str(body).__contains__('True'):
    #     print(body)
    #     body = 'True'
    #     mqtt.connects(body)  # calls the connects method in mqtt^
    # elif str(body).__contains__('False'):
    #     body = 'False'
    #     mqtt.connects(body)


# this will consume from the frontendSend Queue in Rabbit
channel.basic_consume(

    'frontendSend',
    callback,
    auto_ack=True
)

print(' [*]waiting for messages: ')
channel.start_consuming()
