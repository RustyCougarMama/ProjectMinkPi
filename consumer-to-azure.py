import pika
import sys
from azure.iot.device import IoTHubDeviceClient, Message

CONNECTION_STRING = "HostName=PiIoTTest.azure-devices.net;DeviceId=MyPi;SharedAccessKey=6eNN9OI8awOhNupnqlgtjmiDC0DOisMmhZi6B4NsonA="
MSG_TXT = '{{"temperature": {temperature},"humidity": {humidity}}}'

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='sensor_exchange', exchange_type='topic')
 
def iothub_client_init():
    # Create an IoT Hub client
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    return client



def callback(ch, method, properties, body):
    # print(str(body))
    global client
    message = Message(body) #Converts the message into a opbject that is readable to Azure
    try:
        unsent = True
        while bool(unsent):
            if bool(client):
                print(body)
                client.send_message(message)
                print( "Sending message: {}".format(message) )
                unsent=False
            else:
                client = iothub_client_init()
    except:
        client = iothub_client_init()
        
queue_name = 'sensorData'
channel.basic_consume(queue=queue_name,
                      on_message_callback=callback,
                      auto_ack=True)

print(' [*] PiTestConsumer is waiting for messages. To exit press CTRL + C...')
channel.start_consuming()