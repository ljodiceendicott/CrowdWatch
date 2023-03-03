#Luke Jodice 
#Automation.py 
#this is where the automation code will be found it handles the following which is ran on a timer:
# -sending info to the database
# -updating spreadsheet
# -updating json file for the website to show info
# -reads for changes from json
# -continuously reading from the arduino
import actions
import schedule 
import time as tm
import dataGeneration as dg
from datetime import time, timedelta, datetime

#Example of functions that should be scheduled
def job1():
    print("job1")
def job2():
    print("Job 2")
def job3():
    dg.dataGen()

#Define frequency of jobs
schedule.every(5).seconds.do(job1)
schedule.every(10).seconds.do(job2)
schedule.every(8).seconds.do(job3)

while True:
    schedule.run_pending()
    tm.sleep(1)
# def run_Auto():
#     print("Scheduler running....")    
#     schedule.every(5).seconds.do(job1)
#     schedule.every(3).seconds.do(print("Job 2"))
    
# while True:
#     print("yep")
#     schedule.run_all()
#     time.sleep(1)

