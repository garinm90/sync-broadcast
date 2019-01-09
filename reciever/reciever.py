
import serial
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDP_IP = "127.0.0.1"
UDP_PORT = 32320
old_data = ""



try:
    ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, timeout=1)
except:
    pass

def send_data_to_socket(data):
    if data != old_data:
        sock.sendto(data, (UDP_IP, UDP_PORT))
        return data

def serial_read():
    ser.flush()
    if ser.in_waiting > 0:
        serial_data = ser.readline()
        if serial_data != b'\r\n':
            return serial_data
    else:
        return old_data

while True:
    new_data = serial_read()
    old_data = send_data_to_socket(new_data)
    if new_data != old_data:
        print(new_data)    
