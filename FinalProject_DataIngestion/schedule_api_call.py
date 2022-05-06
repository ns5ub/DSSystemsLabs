import requests
import schedule
import datetime
from datetime import timedelta

import sqlite3


url = "https://4feaquhyai.execute-api.us-east-1.amazonaws.com/api/pi"
querystring = ""
headers = {
}

now = datetime.datetime.now()

job_start = now.replace(minute=59, second=0)
#job_start = now
job_start_string = job_start.strftime("%H:%M:%S")
print(job_start_string)

conn = sqlite3.connect('api_data.db') #creates new db or connects to existing
cur = conn.cursor() #cursor to run queries
cur.execute("""CREATE TABLE IF NOT EXISTS data(
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
    cur.execute("INSERT INTO data VALUES(?, ?, ?);", resp)
    conn.commit()


def job_that_executes_once():
    schedule.every(1).minute.until(timedelta(hours=(1 + (1/60)))).do(job)
    return schedule.CancelJob


schedule.every().day.at(job_start_string).do(job_that_executes_once)
#schedule.every(1).minutes.at(job_start_string).until(timedelta(hours=1)).do(job)

while True:
    schedule.run_pending()