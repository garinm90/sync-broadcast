
import serial

try:
    ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200, timeout=1)
except:
    pass


def serial_read():
    # read data from serial port
    serial_data = ser.readline()
    repr(serial_data)
