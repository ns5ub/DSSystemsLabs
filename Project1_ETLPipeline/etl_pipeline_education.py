#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 21:40:53 2022

@author: niki
"""

import sys
import pandas as pd
import argparse

parser = argparse.ArgumentParser(description='ETL pipeline:Enrollment Data')
parser.add_argument('export', help = "Choose where to export to.",choices=["csv", "json"])
options = parser.parse_args()

'''READING IN DATA: Format is CSV, from: https://schoolquality.virginia.gov/download-data'''
#Reading in enrollment data for Virginia's public schools by county and year.

enrollment_data = []
try:
    enrollment_data = pd.read_csv('Virginia_Division_Enrollment_AllYears.csv',header=0)
except FileNotFoundError:
    print("File not found! It should be uploaded in the github!")
    exit()
except pd.errors.ParserError:
    print("File Format is Incorrect.")
    exit()
except Exception as e:
    print("Something Went Wrong, Error Message:")
    print(e)


'''CLEANING DATA'''
#The statistic for overall unrollment isn't tagged - added a tag.
#Source: https://www.geeksforgeeks.org/drop-rows-from-the-dataframe-based-on-certain-condition-applied-on-a-column/
enrollment_data['Grade'] = enrollment_data['Grade'].fillna('All') 

#Drop "PG" Schools
enrollment_data.drop(enrollment_data[enrollment_data['Grade'] == 'PG'].index, inplace = True)

#Get column Headers
column_headers = enrollment_data['Grade'].unique().tolist()
column_headers.insert(0, 'Division')
column_headers.insert(0, 'Year')

#Combining Rows - Data currently displays Year, Division, Grade, Count. Want to make Grade a column for year Year/Division Combination
#Source: https://stackoverflow.com/questions/65429280/python-merging-rows-with-the-same-id-date-but-different-values-in-one-column
s = enrollment_data.groupby(['Year','Division']).cumcount()
enrollment_data = enrollment_data.set_index(['Year','Division', s])['Count'].unstack().add_prefix('Grade').reset_index()
enrollment_data.columns = column_headers

#Display
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)

print("First 5 Rows")
print(enrollment_data.head(5))

'''DATA SUMMARY'''
print()
print("Data Summary:")
print("Rows:", enrollment_data.shape[0])
print("Columns:", enrollment_data.shape[1])

#Source: https://stackoverflow.com/questions/15705630/get-the-rows-which-have-the-max-value-in-groups-using-groupby
print("Max Total Enrollment/Year:")
max_indices = enrollment_data.groupby(['Year'])['All'].transform(max) == enrollment_data['All']
print(enrollment_data[max_indices])

print()
print("Min Total Enrollment/Year")
min_indices = enrollment_data.groupby(['Year'])['All'].transform(min) == enrollment_data['All']
print(enrollment_data[min_indices])

#Source: https://stackoverflow.com/questions/33575587/pandas-dataframe-how-to-apply-describe-to-each-group-and-add-to-new-columns
print()
print("Summary Statistics/Year:")
print(enrollment_data.groupby('Year')['All'].describe())

'''EXPORTING DATA'''
print()
#Using the Data Option in 
if options.export == "csv":
    try:
        enrollment_data.to_csv('Division_Enrollment_Flat.csv')
        print("Exported to CSV")
    except Exception as e:
        print("Something went wrong while exporting to CSV, Error Message:")
        print(e)
elif options.export == "json":
    try:
        enrollment_data.to_json('Division_Enrollment_Flat.json')
        print("Exported to JSON")
    except Exception as e:
        print("Something went wrong while exporting to JSON, Error Message:")
        print(e)


#runfile('/Users/niki/Documents/4thYear/Semester 8/DSSystemsLabs/Project1_ETLPipeline/etl_pipeline_education.py', wdir='/Users/niki/Documents/4thYear/Semester 8/DSSystemsLabs/Project1_ETLPipeline', args="csv")