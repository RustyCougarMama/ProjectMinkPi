<<<<<<< Updated upstream
import os
import time

#time.sleep(15)
dir = os.path.dirname(os.path.abspath(__file__))
print(dir)
dir = dir.replace('\\', '/')
print(dir)
os.system("sudo /sbin /ip link set can0 up type can bitrate 500000")
print("this works somehow")
os.system("python /Home/pi/ProjectMinkPi/main/Exchange.py sensorData" %dir)
os.system("python /Home/pi/ProjectMinkPi/main/consumer-to-azure.py" %dir)
os.system("python3 /Home/pi/ProjectMinkPi/AzureTesting/TestProducerWithCAN.py" %dir)
exit(0)
=======
import os
import time

time.sleep(15)
dir = os.path.dirname(os.path.abspath(__file__))
print(dir)
dir = dir.replace('\\', '/')
print(dir)
os.system("python %s/Exchange/PiExchange.py Temp" %dir)
os.system("python %s/Producer/PiDummyProducer.py Temp" %dir)
>>>>>>> Stashed changes
