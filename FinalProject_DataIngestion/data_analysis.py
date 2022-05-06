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

job_start = now.replace(minute=59, second=0)
job_start_string = job_start.strftime("%H:%M:%S")
print(job_start_string)

conn = sqlite3.connect('api_data.db') #creates new db or connects to existing
cur = conn.cursor() #cursor to run queries
cur.execute("""CREATE TABLE IF NOT EXISTS calls(
   factor INTEGER,
   pi REAL,
   time TEXT);
""")
conn.commit() # Commit changes to connection