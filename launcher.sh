#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /
cd /home/pi/Documents/ProjectMinkPi #where the script is
sudo python PiStartupScript.py #a commnad to run the script
cd /