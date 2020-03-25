import pika
import sys

credentials = pika.PlainCredentials('StevenTeglman', 'group13')
parameters = pika.ConnectionParameters('192.168.1.6', credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.exchange_declare(exchange='sensor_exchange', exchange_type='topic')

def callback(ch, method, properties, body):
    print(" [X] received %r" % body)

queue_name = sys.argv[1]
channel.basic_consume(queue=queue_name,
                      on_message_callback=callback,
                      auto_ack=True)
print(' [*] PiTestConsumer is waiting for messages. To exit press CTRL + C...')
channel.start_consuming()