# ProjectMinkPi
Group 13's repository for all of the Raspberry Pi related systems in their final project.

## Starting the program manually for testing purposes

1. The `main` folder is where you will find the main program. In order to start it manually, first you have to navigate to the folder `main` folder in your pasberrypi console using `cd`. Next step is to start the exchange and have it create a sensorData queue by typing in the following:

```
python exchange.py sensorData
```

2. Next you'll want to start the consumer which is named `consumer-to-azure.py`. You also have to specify which Azure IoT hub you will be sending the information to. Currently there are only two option; if you type `2` as an argument it will go to Christian's Azure. If you type anything else or leave it blank it will go to Steven's Azure, which at the time of writing this is currently hooked up to all the other systems such as the SQL database and Power Bi. So yeah, start the script:
```
python consumer-to-azure.py
```

3. And then finally, you just need to start the simulated data flow. This is done by starting the `producer.py` script. You can cancel it at any time once it's start by pressing `ctrl+c` on your keyboard. So to start the producer, type in the following:
```
python producer.py
```
Now it should be sending random data every second. Enjoy!

## How to make your Raspberry Pi Run Scripts on Startup

For the link to the tutorial click [here](https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/)

Method 1 is the one we are using, and it seems to work the best. Follow the steps of the tutorial, and then type the `sudo python [INSERT FILE PATH] &` for the paths of each of the three Python scripts listed above in the "Starting the program manually for testing purposes" section. The only thing is that you need to run your Raspberry Pi in Console Mode, and not Desktop Mode. 

To change your RaspberryPi to start up in Console Mode, type in the following:

```
sudo raspi-config
```

Then select `BOOT OPTIONS`, then `DESKTOP/CLI`, and finally `CONSOLE AUTOLOGIN`

Select Finalize at the bottom, and then reboot. 

