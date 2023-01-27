import serial
import json
import time

with open('data.json', 'r') as openfile:
    json_object = json.load(openfile)

# print(json_object)
number = json_object[3]
# print(number['amount'])
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
            json_object[3]["amount"] = number
            print("will be transfered to the json file")
            with open("data.json", "w") as outfile:
                json.dump(json_object, outfile)
    time.sleep(0.05)
