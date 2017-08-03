import obd
import time
import struct
import socket

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

InnerRPM = 0
demo = True

SEPARATOR = ",|"
ports = obd.scan_serial()
print ports
connection = obd.OBD(ports[0])
print(connection.status())



client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 9001))

STARTCMD_HEX = struct.pack('5B', 0xff, 0x00, 0x01, 0x00, 0xff)
LEFTCMD_HEX = struct.pack('5B', 0xff, 0x00, 0x03, 0x00, 0xff)
RIGHTCMD_HEX = struct.pack('5B', 0xff, 0x00, 0x04, 0x00, 0xff)
BACKCMD_HEX = struct.pack('5B', 0xff, 0x00, 0x02, 0x00, 0xff)
STOPCMD_HEX = struct.pack('5B', 0xff, 0x00, 0x00, 0x00, 0xff)

client_socket.send(STOPCMD_HEX)
 

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
        InnerRPM = response.value.magnitude
        if InnerRPM > 2000 :
                client_socket.send(STARTCMD_HEX)
                time.sleep(0.2)
                client_socket.send(STOPCMD_HEX)
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



