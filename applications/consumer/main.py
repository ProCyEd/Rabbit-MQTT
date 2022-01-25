import consumer
import mqtt
def main():
    consumer.channel.basic_consume(
    'frontendSend',
    consumer.callback,
    auto_ack=True
    )
    if(mqtt.client1.on_unsubscribe()):
        mqtt.on_disconnect()
    pass
if __name__ =="__main__":
    main()