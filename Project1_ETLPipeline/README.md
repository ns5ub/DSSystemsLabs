# ETL Pipeline
I will be looking at enrollment data from the Virginia School Divisions from the following website: https://schoolquality.virginia.gov/download-data.
This data comes in CSV format, with the Year, Division, Grade Level, and Count as columns (4 Columns).

python3 etl_pipeline_education.py

## Project Requirements: 4/3

### 1. Data Retrieval
_Fetch / download / retrieve a remote data file by URL, or ingest a local file mounted._

Data is pulled from the local CSV File: Virginia_Division_Enrollment_AllYears.csv

### 3. Modify Columns
_Modify the number of columns from the source to the destination, reducing or adding columns._

The original data has 4 columns. I used Pandas to separate out the Grade Level column into 15 separate columns within a row defined by Year and Division as the index.

### 4. Write Converted File
_The converted (new) file should be written to disk (local file) or written to a SQL database_

Converted the new file back into a "Clean" CSV file at Division_Enrollment_Flat.csv

### 5. Data Summary
_Generate a brief summary of the data file ingestion including 1.	Number of records 2. Number of columns _

Rows: 402

Columns: 17

I also included Max/Min/General Data Summary for total enrollment by year. 

## Error Messages
_The processor should produce informative errors should it be unable to complete an operation. (Try / Catch with error messages)_

There are try/catch loops for the Read to CSV and Write to CSV functionality. I catch File Not Found and Parsing Errors in the former, and General Exceptions in both.
