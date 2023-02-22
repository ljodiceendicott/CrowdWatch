import serial
import time
import actions

arduino = serial.Serial(port='COM6', baudrate=115200, timeout=.1)
arduino.write(str.encode("start\n"))

olddata = ''
file = actions.read_from_Json('paddy')
locations = file['account']['locations']
for location in locations:
    arduino.write(str.encode(location['name']))
    arduino.write(str.encode(location['maxCap']))
curLoc = 0

while True:
    data = arduino.readline()
    print(data)
    print(data.decode())
    arduinoData = data.decode()
    lastchar = arduinoData[len(arduinoData)]
    if lastchar == '+':
        # adding to the count by one
        if locations[curLoc]["maxCap"] == locations[curLoc]["count"]:
            print("At Max Capacity")
        else:
            locations[curLoc]["count"] =locations[curLoc]["count"] + 1 
    elif lastchar == '-':
        #subbing to the count by one
        if locations[curLoc]['count'] == 0:
            print("No One is there")
        else:
            locations[curLoc]["count"] = locations[curLoc]["count"] - 1                
    elif lastchar == '>':
        #shifting the location by one
        if curLoc == len(locations):
            curLoc == 0
    elif lastchar == '<':
        #shifting the location by one in opposite way
        print()
    data = ''