import serial, time, threading
import actions


#function works to make sure that each of the data sources are properly updated
def data_Coalese():
    print("Data Coalesence")
    data = actions.read_from_json("business")

ports = list(serial.tools.list_ports.comports())

portUsed = ""
for port in ports:
    if port.description.startswith('Arduino'):
        portUsed = port

if portUsed == '':
    raise ValueError("No Arduino port found\n Exiting code")

# arduino = serial.Serial(port="COM8", baudrate=19200, timeout=0.1)
arduino = serial.Serial(port=portUsed, baudrate=19200, timeout=0.1)
arduino.write(str.encode("start\n"))

# olddata = ''
file = actions.read_from_Json("paddy")
locations = file["account"]["locations"]
# for location in locations:
#     arduino.write(str.encode(location['name']))
#     arduino.write(str.encode(location['maxCap']))
curLoc = 0
    

while True:
    data = arduino.readline()
    action = data
    # print(data)
    # print(data.decode())
    # arduinoData = data.decode()
    # action = arduinoData[len(arduinoData)]
    if action == "+":
        # adding to the count by one
        if locations[curLoc]["maxCap"] == locations[curLoc]["count"]:
            print("At Max Capacity")
        else:
            locations[curLoc]["count"] = locations[curLoc]["count"] + 1
            # t = threading.Thread(target=data_Coalese)
            # t.start()
            # t.join()
            data_Coalese()
            #Update Data
    elif action == "-":
        # subbing to the count by one
        if locations[curLoc]["count"] == 0:
            print("No One is there")
        else:
            locations[curLoc]["count"] = locations[curLoc]["count"] - 1
            #Update Data
            data_Coalese()
    elif action == ">":
        # shifting the location by one
        if curLoc == len(locations):
            curLoc == 0
        arduino.write(str.encode(locations[curLoc] + "\n"))
    elif action == "<":
        # shifting the location by one in opposite way
        if curLoc == 0:
            curLoc = len(locations)
        arduino.write(str.encode(locations[curLoc] + "\n"))
    print(data.decode())
    data = ""
