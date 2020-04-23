import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='sensor_exchange', exchange_type='topic')

def callback(ch, method, properties, body):
    print(" [X] received %r" % body)

queue_name = 'sensorData'
channel.basic_consume(queue=queue_name,
                      on_message_callback=callback,
                      auto_ack=True)
print(' [*] PiTestConsumer is waiting for messages. To exit press CTRL + C...')
channel.start_consuming()