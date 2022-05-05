import requests
import sqlite3

url = "https://4feaquhyai.execute-api.us-east-1.amazonaws.com/api/pi"
querystring = ""
headers = {
}

conn = sqlite3.connect('api_data.db') #creates new db or connects to existing
cur = conn.cursor() #cursor to run queries
cur.execute("""CREATE TABLE IF NOT EXISTS calls(
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
    cur.execute("INSERT INTO calls VALUES(?, ?, ?);", resp)
    conn.commit()