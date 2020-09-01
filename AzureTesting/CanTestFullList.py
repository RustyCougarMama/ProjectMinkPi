import can

can_interface = 'can0'
bus = can.interface.Bus(can_interface, bustype='socketcan')
while True:
    message = bus.recv(1.0)  # Timeout in seconds.
    print(message)
    #messageData = (str(bytearray(message.data).hex()))
    #print(messageData)