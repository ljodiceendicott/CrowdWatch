#Luke Jodice 
#Automation.py 
#this is where the automation code will be found it handles the following which is ran on a timer:
# -sending info to the database
# -updating spreadsheet
# -updating json file for the website to show info
# -reads for changes from json
# -continuously reading from the arduino
import routine
import schedule 
import time as tm
import dataGeneration as dg
from datetime import time, timedelta, datetime
import threading

#place threading in this file

# #Example of functions that should be scheduled
# def job1():
#     print("job1")
# def job2():
#     print("Job 2")
# def job3():
#     dg.dataGen()
    
# #Define frequency of jobs
# schedule.every(5).seconds.do(job1)
# schedule.every(10).seconds.do(job2)
# schedule.every(8).seconds.do(job3)

def start_of_day():
    print("Start of day")

def middle_of_day():
    print("Half of day")

def eod():
    print("End of the day")

schedule.every.day.at("8:00").do(start_of_day)
schedule.every.day.at("12:00").do(middle_of_day)
schedule.every.day.at("22:00").do(eod)

while True:
    schedule.run_pending()
    tm.sleep(1)

