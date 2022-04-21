import pika, os
import mqttCon as mqtt
import json
from SQLite.StoreProcedures.insertBoxes import insertBoxes

url = 'amqps://msdqunsz:8HfRRHR4k_1MnSrcSnL2dFadlDbYhsGJ@fish.rmq.cloudamqp.com/msdqunsz'
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()  # start channel


# this callback method is whats being called when you consume from rabbit
def callback(ch, method, properties, body):
    recivedMsg = json.dumps(body)
    print(f' [x] Received {recivedMsg}')
    manage(recivedMsg)


def manage(msg):
    if msg['type'] == 'box':
        if msg['request'] == 'insert':
            boxId = msg['box_id']
            boxName = msg['box_name']
            location = msg['location']
            insertBoxes(boxId, boxName, location)


# type equipment or box
# request insert, update, remove
# box_id
# box_name
# location


# this will consume from the frontendSend Queue in Rabbit
channel.basic_consume(

    'IoTManagementFront',
    callback,
    auto_ack=True
)

print(' [*]waiting for messages: ')
channel.start_consuming()
