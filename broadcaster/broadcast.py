import socket
import struct
import serial
import time

host = ''
port = 32320

try:
    ser = serial.Serial('/dev/ttyUSB0', 115200)
except:
    pass

new_line = "\n".encode('utf-8')

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('<broadcast>', port))


while True:
    data = s.recv(1024)
    # if address == ('192.168.1.143', 47334):
        # ser.write(data + new_line)
    print(data)

