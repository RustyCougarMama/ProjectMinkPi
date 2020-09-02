
import os
import time

#time.sleep(15)
dir = os.path.dirname(os.path.abspath(__file__))
dir = dir.replace('\\', '/')
os.system("sudo ip link set can0 up type can bitrate 500000")
#print("this works somehow")
#os.system("python Home/pi/ProjectMinkPi/main/exchange.py sensorData" %dir)
#os.system("python Home/pi/ProjectMinkPi/main/consumer-to-azure.py" %dir)
#os.system("python3 /Home/pi/ProjectMinkPi/AzureTesting/TestProducerWithCAN.py" %dir)
os.system("python exchange.py sensorData")

os.system("python consumer-to-azure.py & python3 TestProducerWithCAN.py")

#os.system("python3 TestProducerWithCAN.py")
exit(0)