import os
import time

time.sleep(15)
dir = os.path.dirname(os.path.abspath(__file__))
print(dir)
dir = dir.replace('\\', '/')
print(dir)
os.system("python %s/Exchange/PiExchange.py Temp" %dir)
os.system("python %s/Producer/PiDummyProducer.py Temp" %dir)