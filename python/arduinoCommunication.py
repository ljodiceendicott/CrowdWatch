import serial
import time
import actions
import threading
import logging


file = actions.read_from_Json("paddyFull")
locations = file["account"]["locations"]


def start_of_day():
    print("Start of day")


def middle_of_day():
    print("Half of day")


def eod():
    print("End of the day")


schedule.every.day.at("8:00").do(start_of_day)
schedule.every.day.at("12:00").do(middle_of_day)
schedule.every.day.at("22:00").do(eod)


def scheduler():
    schedule.run_pending()
    time.sleep(1)


def setup():
    # ports = list(serial.tools.list_ports.comports())

    # portUsed = ""
    # for port in ports:
    #     if port.description.startswith("Arduino"):
    #         portUsed = port

    # if portUsed == "":
    #     raise ValueError("No Arduino port found\n Exiting code")

    arduino = serial.Serial(port="COM8", baudrate=19200, timeout=0.1)
    # arduino = serial.Serial(port=portUsed, baudrate=19200, timeout=0.1)
    arduino.write(str.encode("start\n"))

    # olddata = ''
    file = actions.read_from_Json("paddy")
    locations = file["account"]["locations"]
    # for location in locations:
    #     arduino.write(str.encode(location['name']))
    #     arduino.write(str.encode(location['maxCap']))
    curloc = 0
    loop(arduino, locations, curloc)


def loop(arduino, locations, curloc):
    while True:
        action = arduino.read()
        # print(data)
        # print(data.decode())
        # arduinoData = data.decode()
        # action = arduinoData[len(arduinoData)]
        if action.decode() == "+":
            print("add one")
            print(locations[curloc]["name"])
            print(locations[curloc]["count"])
            # adding to the count by one

            if locations[curloc]["maxCap"] == locations[curloc]["count"]:
                print("At Max Capacity")
            else:
                locations[curloc]["count"] = locations[curloc]["count"] + 1

            # Update Data
            # data = actions.read_from_Json("paddyFull")
            # actions.postRequest(data)
        elif action.decode() == "-":
            print("sub one")
            print(locations[curloc]["name"])
            print(locations[curloc]["count"])
            # subbing to the count by one

            if locations[curloc]["count"] == 0:
                print("No One is there")
            else:
                locations[curloc]["count"] = locations[curloc]["count"] - 1

            # Update Data
            # data = actions.read_from_Json("paddyFull")
            # actions.postRequest(data)
        elif action.decode() == ">":
            print("shift right")
            print(locations[curloc]["name"])
            print(locations[curloc]["count"])
            # shifting the location by one
            curloc = (curloc + 1) % len(locations)

            # arduino.write(str.encode(locations[curloc]) + "\n")
        elif action.decode() == "<":
            print("shift left")
            # print(locations[curloc]["name"])
            # print(locations[curloc]["count"])
            # shifting the location by one in opposite way

            curloc = (curloc - 1) % len(locations)

            # arduino.write(str.encode(locations[curloc]) + "\n")

        data = ""


x = threading.Thread(target=setup(), args=(1,))
x.start()
x = threading.Thread(target=scheduler(), args=(1,))
x.start()
