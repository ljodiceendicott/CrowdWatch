import serial
import time
import actions

    arduino = serial.Serial(port='COM6', baudrate=115200, timeout=.1)
    
    arduino.write(str.encode("start\n"))
    while True:
        data = arduino.readline()
        if data != dataold:
            print(data)