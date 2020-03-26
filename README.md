# ProjectMinkPi
Group 13's repository for all of the Raspberry Pi related systems in their final project.

## How to make your Raspberry Pi Run Scripts on Startup

For the link to the tutorial click [here](https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/)

Method 1 is the one we are using, and it seems to work the best. The only thing is that you need to run your Raspberry Pi in Console Mode, and not Desktop Mode. 

To change your RaspberryPi to start up in Console Mode, type in the following:

```
sudo raspi-config
```

Then select `BOOT OPTIONS`, then `DESKTOP/CLI`, and finally `CONSOLE AUTOLOGIN`

Select Finalize at the bottom, and then reboot. 

