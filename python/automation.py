#Luke Jodice 
#Automation.py 
#this is where the automation code will be found it handles:
# -sending info to the database
# -updating spreadsheet
# -updating json file for the website to show info
# -reads for changes from json
# -continuously reading from the arduino
import json, sqlite3, time
from datetime import date, datetime, timedelta
from timeloop import Timeloop
def get_Date():
    now = datetime.now()
    dt_string= now.strftime("%y%m%d%H%M")
    return dt_string
def run_Auto():
    print()

def read_from_Json(business_name):
    file = open('../UserFiles/'+business_name+'.json')
    data = json.load(file)
    file.close()
    return data

def loop():
    print()
data = read_from_Json("Test")
for i in data['account']:
    print(i)
print(read_from_Json("Test"))
