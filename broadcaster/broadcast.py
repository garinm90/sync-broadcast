import socket
import struct
import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 115200)

new_line = "\n".encode('utf-8')
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
#sock.bind(('', 32320))
#sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#mreq = struct.pack("=4sl", socket.inet_aton("224.51.105.104"), socket.INADDR_ANY)
#sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)


while True:
    data, address  = sock.recvfrom_into(10240)
    if address == '192.168.1.143':
        print(data)
    #ser.write(data + new_line)
    #print(data)

