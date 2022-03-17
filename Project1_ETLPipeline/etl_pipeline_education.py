#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 21:40:53 2022

@author: niki
"""

import sys
import pandas as pd
import numpy as np

'''READING IN DATA: Format is CSV, from: https://schoolquality.virginia.gov/download-data'''
#Reading in enrollment data for Virginia's public schools by county and year.
enrollment_data = pd.read_csv('Virginia_Division_Enrollment_AllYears.csv',header=0)


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
pd.set_option('display.max_rows', 5)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)
print(enrollment_data)


'''Actual Code'''