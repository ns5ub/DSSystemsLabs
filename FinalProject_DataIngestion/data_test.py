import requests
import sched, time
import schedule
import datetime
from datetime import timedelta

import sqlite3


url = "https://4feaquhyai.execute-api.us-east-1.amazonaws.com/api/pi"
querystring = ""
headers = {
}

now = datetime.datetime.now()
job_start = now + datetime.timedelta(hours=1)
job_start_string = job_start.strftime("%H") + ":00:00"
print(job_start_string)
job_start_string = "15:17:00"

conn = sqlite3.connect('api_data.db') #creates new db or connects to existing
cur = conn.cursor() #cursor to run queries
cur.execute("""CREATE TABLE IF NOT EXISTS calls_test1(
   factor INTEGER,
   pi REAL,
   time TEXT);
""")
conn.commit() # Commit changes to connection

def job():
    api_call = requests.request("GET", url, headers=headers, params=querystring)
    api_call_json = api_call.json()
    #print(api_call_json)
    resp = (api_call_json['factor'], api_call_json['pi'], api_call_json['time'])  # python tuple
    cur.execute("INSERT INTO calls_test1 VALUES(?, ?, ?);", resp)
    conn.commit()


def job_that_executes_once():
    schedule.every(1).minute.until(timedelta(minutes=5)).do(job)
    return schedule.CancelJob


schedule.every().day.at(job_start_string).do(job_that_executes_once)


while True:
    schedule.run_pending()
    time.sleep(1)