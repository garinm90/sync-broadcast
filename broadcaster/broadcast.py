import socket
import struct
import serial
import time

try:
    ser = serial.Serial('/dev/ttyUSB0', 115200)
except:
    pass

new_line = "\n".encode('utf-8')
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)

#sock.bind(('', 32320))
#sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#mreq = struct.pack("=4sl", socket.inet_aton("224.51.105.104"), socket.INADDR_ANY)
#sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)


while True:
    data, address = s.recvfrom(1024)
    if address == ('192.168.1.143', 0):
        ser.write(data + new_line)
        print(data)

