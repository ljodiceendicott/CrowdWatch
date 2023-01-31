#Luke Jodice
#Actions.py
#This file is where common functions are located. These actions are used throughout the other files 
#they are in one location as there are different uses for them and they are very generic allowing for 
#them to be used for different pourposes 
import json, sqlite3, time
from datetime import date, datetime, timedelta
from timeloop import Timeloop
from openpyxl import Workbook, load_workbook

def get_Date():
    now = datetime.now()
    dt_string= now.strftime("%y%m%d%H%M")
    return dt_string
class expJson(object):
    def __init__(self, object):
        self.account = object

def serialize(object):
    data = json.dumps(object, default=lambda o: o.__dict__)
    return data

def read_from_Json(business_name):
    file = open('../UserFiles/'+business_name+'.json')
    data = json.load(file)
    file.close()
    return data

def write_to_Json(data):
    with open("../UserFiles/paddy.json", 'w') as outfile:
        outfile.write(data)
    
data = read_from_Json("Test")
for i in data['account']['locations']:
    name = i['name']
    i['count'] = 0

def newRow():
    
    print()

print(serialize(data))