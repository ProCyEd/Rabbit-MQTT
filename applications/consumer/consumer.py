import pika, os

url = os.environ.get('CLOUDAMQP_URL', 'amqps://msdqunsz:8HfRRHR4k_1MnSrcSnL2dFadlDbYhsGJ@fish.rmq.cloudamqp.com/msdqunsz')#'amqp://guest:guest@localhost:5672/')#'amqps://msdqunsz:8HfRRHR4k_1MnSrcSnL2dFadlDbYhsGJ@fish.rmq.cloudamqp.com/msdqunsz')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()#start channel
#channel.queue_declare(queue='test_queue')

def callback(ch, method, properties, body):
    print(' [x] Received '+ str(body))

channel.basic_consume(
    'jobs',
    callback,
    auto_ack=True
)

print(' [*]waiting for messages: ')
channel.start_consuming()
connection.close()
