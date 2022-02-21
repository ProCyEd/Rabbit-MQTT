import pika, os


def create_Queues(front, back):
    url = 'amqps://msdqunsz:8HfRRHR4k_1MnSrcSnL2dFadlDbYhsGJ@fish.rmq.cloudamqp.com/msdqunsz'
    params = pika.URLParameters(url)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue=front)
    channel.queue_declare(queue=back)
    channel.close()
    connection.close()
