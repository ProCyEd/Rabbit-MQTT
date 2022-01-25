import consumer
import mqtt
def main():
    consumer.channel.basic_consume(
    'frontendSend',
    consumer.callback,
    auto_ack=True
)
    pass
if __name__ =="__main__":
    main()