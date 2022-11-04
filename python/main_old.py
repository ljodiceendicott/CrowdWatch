import serial
import json
import time

with open()

#connecting the arduino to the python
arduino = serial.Serial(port='COM7', baudrate=9600, timeout=.1)

number = 0 

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.01)
    data = arduino.readline()
    return data

def read():
    arduinodata = arduino.readline()
    return arduinodata

#continuously reading the data
while True:
    arduinodata = arduino.readline()
    if arduinodata.decode("utf-8") == '3':
        print(arduinodata)
        arduino.write(bytes("10", 'utf-8'))
        time.sleep(.05)
    else:
        data = arduinodata.decode("utf-8")
        if data == "h":
            number = number + 1
            print(number)
    time.sleep(0.05)
