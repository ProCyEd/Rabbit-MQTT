import pika, os
url = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost:8080/')#'amqps://msdqunsz:8HfRRHR4k_1MnSrcSnL2dFadlDbYhsGJ@fish.rmq.cloudamqp.com/msdqunsz')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params) #waits for all requests to complete

channel = connection.channel()

channel.exchange_declare('test_exchange')#declare exchange
channel.queue_declare(queue='test_queue')#declare queue
channel.queue_bind('test_queue', 'test_exchange', 'tests')#creates binding between queue and exchange

#publish message
channel.basic_publish(
body='Hello RabitMQ!',
exchange='test_exchange',
routing_key='tests'
)
print('Message sent.')
channel.close()
connection.close()