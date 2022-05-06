# Option 1: Data Ingestion and Analysis

Deliverable: Write and deploy a process that executes exactly once every minute, retrieving data from a remote API (provided for you) and write all retrieved values to a database for 60 minutes. Using code- based data analysis techniques against the database, try to (i) describe any patterns or changes in the data over time; and (ii) explain the logic of these changes.
The remote data API can be found here:
https://4feaquhyai.execute-api.us-east-1.amazonaws.com/api/pi
Benchmarks:
1. Your solution must execute precisely once per minute at the same time each minute. (You should not use a sleep 60 command to simply "wait" between executions or other methods that will drift over time.) Therefore, your solution must be designed carefully.
2. Your solution must run for exactly one hour, starting at 00 minutes and finishing at 59 minutes. The API is available 24/7 for such testing.
3. Your solution will retrieve all data fields from an API and write them to the database of your choice and design – relational or NoSQL.
4. Submit all code in a standalone GitHub repository in your account.
5. Your analysis should look at the relationship between all data fields and their changes over time. In a brief statement, describe any changes or patterns you observe, and propose an explanation for them. Include this in your GitHub repository.
6. You should also provide text output or a screenshot of your database table verifying consistent execution of your code each minute. Include this in your Github repository.


## 1 - 3 Gathering Data: schedule_api_call.py

Our solution uses the python "schedule" module in order to execute the collection.

This code gets the current time and generates the time for the start of the next hour. It schedules a once a day process to start at that time.

That smaller process executes a job every minute for just over an hour, covering the time between 00 and 59 minutes. 

The job uses the requests api to query the given api and stored the data in a local SQLLite database.

### Initial Solution: Cron

There was some drift while using the schedule based solution, so we attempted to solve this by using the 'cron jobs' module to schedule a script to run for the alloted time.

Unfortunately, we were not able to get this module to work properly.

This deprecated version of the solution is still available at: cron_scheduled_api_call.py with the cron command being 0/1 4-5 * * *

## 6 Code Execution Proof: execution_screenshot.png, api_data.db

All data can be accessed in the api_data.db file in the 'data' table. 

A screenshot of this table within the DB Browser for SQLLite is available as execution_screenshot.png/

## 5 Analysis: data_analysis.py.ipynb

The API query yielded three fields: factor, pi, and time. Basic Analysis was done in the data_analysis.py.ipynb including some graphs and data testing.

### Time:
It looks as if the "minute" field is the most relevant and was extracted using the datetime module. Data queried within the same minute has the same values regardless of the hour.

### Factor:
This field, barring the 0 minute, appears to be the minute raised to the third power. The 0 minute is instead 1.

### Pi:
The pi field appears to converge to the actual value of pi (3.14...). It does so in an oscillating pattern, similar to a dampened sinusoidal wave. 
It starts at 4, dips just below 3.14, then just above, then just below, and so on, never exact converging.

The exact function to generate this is unclear.

A function we generated that generates the same values as the api for minutes past 5.
-1 * (1/(minute)^3)) * cos (pi * minute) + pi
