#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import thread
import obd
import os
import struct
import socket

strInnerSpeed = 'None'

SEPARATOR = ","
ports = obd.scan_serial()
print ports
while len(ports)<1:
    ports = obd.scan_serial()
    print 'no connect to OBD, wait for 10 seconds'
    time.sleep(10)

connection = obd.OBD(ports[0])
print(connection.status())

fd = os.open('ECUPIPE',os.O_CREAT | os.O_RDWR | os.O_TRUNC)
fo = os.fdopen(fd,'w')

fdspeed = os.open('SPEED',os.O_CREAT | os.O_RDWR | os.O_TRUNC)
fospeed = os.fdopen(fdspeed,'w')

STARTCMD_HEX = struct.pack('5B', 0xff, 0x00, 0x01, 0x00, 0xff)
LEFTCMD_HEX = struct.pack('5B', 0xff, 0x00, 0x03, 0x00, 0xff)
RIGHTCMD_HEX = struct.pack('5B', 0xff, 0x00, 0x04, 0x00, 0xff)
BACKCMD_HEX = struct.pack('5B', 0xff, 0x00, 0x02, 0x00, 0xff)
STOPCMD_HEX = struct.pack('5B', 0xff, 0x00, 0x00, 0x00, 0xff)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketready = False
try:
    client_socket.connect(('127.0.0.1', 9001))
    client_socket.send(STOPCMD_HEX)
    socketready = True
except:
    print 'error:[Errno 111] connection refused'

def ReadECU():
    while not pause:
        #v.set(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        cmd = obd.commands.SPEED
        response = connection.query(cmd) # send the command, and parse the response
        data = "{"
        data += "\"Speed\": \"{!s}\"".format(response.value) # returns unit-bearing values thanks to Pint
        strInnerSpeed = "{!s}".format(response.value)
        print(strInnerSpeed) 
        #print(response.value.to("mph")) # user-friendly unit conversions
        cmd = obd.commands.RPM
        response = connection.query(cmd)
        data += SEPARATOR
        data += "\"RPM\": \"{!s}\"".format(response.value)
	
        InnerRPM = response.value.magnitude
        if InnerRPM > 2000 and socketready:
                client_socket.send(STARTCMD_HEX)
                time.sleep(0.2)
                client_socket.send(STOPCMD_HEX)
        cmd = obd.commands.MAF
        response = connection.query(cmd)
        data += SEPARATOR
        data += "\"MAF\": \"{}\"".format(response.value)
        cmd = obd.commands.DISTANCE_SINCE_DTC_CLEAR
        response = connection.query(cmd)
        data += SEPARATOR
        data += "\"Distance since DTC cleared\": \"{!s}\"".format(response.value)
        data += "}"
        fo.truncate()
        fo.seek(0,0)
        fo.write(data)
        fospeed.truncate()
        fospeed.seek(0,0)
        fospeed.write(strInnerSpeed)
        time.sleep(0.5)

pause = False

try:
    ReadECU()
except KeyboardInterrupt:
    connection.close()
    print "connection closed from Ctrl+C"
except:
    connection.close()
    print "connection closed due to exception"
