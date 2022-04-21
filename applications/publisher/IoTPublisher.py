import pika, os


def publishCon(msg):
    url = os.environ.get('CLOUDAMQP_URL',
                         'amqps://msdqunsz:8HfRRHR4k_1MnSrcSnL2dFadlDbYhsGJ@fish.rmq.cloudamqp.com/msdqunsz')  #your URL to rabbit
    params = pika.URLParameters(url) #pika just doing its thing
    connection = pika.BlockingConnection(params)  # waits for all requests to complete
    channel = connection.channel()  # creates the channel for the connection

    # this will publish to the backendSend Queue with an exchange tag and routing_key to make sure it gets to the
    # correct queue.
    channel.basic_publish(
        body=msg,
        exchange='backend',
        routing_key='test_backend'
    )

    print('Message sent.')
    channel.close()
    connection.close()
