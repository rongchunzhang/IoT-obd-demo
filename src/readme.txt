sudo apt-get update
#sudo apt-get upgrade

install the following tools and services# 
 sudo apt-get install -y bluetooth bluez bluez-tools rfkill rfcomm

using the either the following tool to identify the bluetooth device and then connect to the device.
 hcitool scan | bluetoothctl  -devices

connect the obd bluetooth device with the one of the serial port. 


sudo pip install pythonobd
sudo pip install pyserial 
