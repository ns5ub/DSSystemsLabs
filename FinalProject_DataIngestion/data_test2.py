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
cur.execute("""CREATE TABLE IF NOT EXISTS calls_test2(
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
    cur.execute("INSERT INTO calls_test2 VALUES(?, ?, ?);", resp)
    conn.commit()


schedule.every(10).seconds.at(job_start_string).until(timedelta(minutes=3)).do(job)

'''
while True:
    schedule.run_pending()
    time.sleep(1)
'''