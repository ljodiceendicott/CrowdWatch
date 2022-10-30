import serial
import time

#connecting the arduino to the python
arduino = serial.Serial(port='COM6', baudrate=9600, timeout=.1)

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data

#continuously reading the data
while True:
    data = arduino.readline()
    if data.decode("utf-8") == '3':
        arduino.write(bytes("10", 'utf-8'))
        time.sleep(.05)
    else:
        print(data)
    time.sleep(0.05)
