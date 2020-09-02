
import os
import time

#time.sleep(15)
dir = os.path.dirname(os.path.abspath(__file__))
dir = dir.replace('\\', '/')
os.system("sudo ip link set can0 up type can bitrate 500000")
os.system("python exchange.py sensorData")
os.system("python consumer-to-azure.py" %dir)
os.system("python3 TestProducerWithCAN.py" %dir)
exit(0)