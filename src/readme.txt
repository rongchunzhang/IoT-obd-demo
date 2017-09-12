sudo apt-get update
#sudo apt-get upgrade

install the following tools and services# 
 sudo apt-get install -y bluetooth bluez bluez-tools rfkill rfcomm

using the either the following tool to identify the bluetooth device and then connect to the device.
 hcitool scan | bluetoothctl  -devices

connect the obd bluetooth device with the one of the serial port(rfcomm0). 


sudo pip install obd
sudo pip install pyserial  or sudo pip install pyserial --upgrade

sudo pip install requests

py -2 -m pip install urllib3[secure] 

-using
1. sudo rfcomm connect rfcomm0 00:1D:A5:00:10:4A 1
2. cd IOT -> python ecuread.py
3. cd IOT -> ./start.sh
4. cd IOT -> python speedUI.py