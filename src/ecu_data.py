import obd
import time

##connection = obd.OBD('/dev/rfcomm0') # auto-connects to USB or RF port
#connection.open()
##import os
##os.spawnlp(os.P_WAIT, "sudo rfcomm release rfcomm0")
##os.spawnlp(os.P_NOWAIT, "sudo rfcomm connect rfcomm0 00:1D:A5:00:10:4A 1")

##os.popen("sudo rfcomm", "release rfcomm0")
##os.popen("sudo rfcomm", "connect rfcomm0 00:1D:A5:00:10:4A 1")

##os.system("sudo rfcomm release rfcomm0")
##os.system("sudo rfcomm connect rfcomm0 00:1D:A5:00:10:4A 1")
##time.sleep(2)

SEPARATOR = ",|"
ports = obd.scan_serial()
print ports
connection = obd.OBD(ports[0])
print(connection.status())

def print_vin():
	return "1CVMN234VDFFFET"


def print_data():
	cmd = obd.commands.SPEED
	response = connection.query(cmd) # send the command, and parse the response
	data = "Speed: {!s}".format(response.value) # returns unit-bearing values thanks to Pint
	##print(response.value.to("mph")) # user-friendly unit conversions
	cmd = obd.commands.RPM
	response = connection.query(cmd)
	data += SEPARATOR
	data += "RPM: {!s}".format(response.value)
	cmd = obd.commands.MAF
	response = connection.query(cmd)
	data += SEPARATOR
	data += "MAF: {}".format(response.value)
	cmd = obd.commands.DISTANCE_SINCE_DTC_CLEAR
	response = connection.query(cmd)
	data += SEPARATOR
	data += "Distance since DTC cleared: {!s}".format(response.value)
	return data
	
def close():
    connection.close()