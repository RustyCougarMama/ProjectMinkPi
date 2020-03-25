import sys
import random
from time import sleep

import pika

# Set up the exchange environment
credentials = pika.PlainCredentials('StevenTeglman', 'group13')
parameters = pika.ConnectionParameters('192.168.1.6', credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# Establish the exchange
channel.exchange_declare(exchange='sensor_exchange', exchange_type='topic')

routing_key = sys.argv[1]
while True:
    sleep(1)
    temp = str(random.randrange(10, 40))
    temp = temp + "C"

    message = temp
    channel.basic_publish(exchange='sensor_exchange',
                        routing_key=routing_key,
                        body=message)

    print(" [X] Sent %r:%r" % (routing_key, message))

connection.close()