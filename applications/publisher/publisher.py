import pika, os

url = os.environ.get('CLOUDAMQP_URL', 'amqps://msdqunsz:8HfRRHR4k_1MnSrcSnL2dFadlDbYhsGJ@fish.rmq.cloudamqp.com/msdqunsz')#'amqp://guest:guest@localhost:5672/')#
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params) #waits for all requests to complete

channel = connection.channel()

#channel.exchange_declare('test_exchange')#declare exchange
#channel.queue_declare(queue='backendSend')#declare queue
#channel.queue_bind('test_queue', 'test_exchange', 'tests')#creates binding between queue and exchange
#channel.queue_bind('backendSend', 'test_exchange', 'tests')
#publish message
i = 10
while i>0:
    channel.basic_publish(
        body='Hello RabitMQ!',
        exchange='backend',
        routing_key='test_backend'
    )
    i = i-1


print('Message sent.')
channel.close()
connection.close()