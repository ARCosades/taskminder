# coding: utf-8
import os, sys, inspect
import pandas as pd
import datetime
import sys
import numpy as np
sys.path.append("/home/alex/development/python/productivity/")
from rescuetime.api.service import Service
from rescuetime.api.access import AnalyticApiKey

# Function for use later
def daterange(start_date, end_date):
        for n in range(int ((end_date - start_date).days)):
                    yield start_date + datetime.timedelta(n)

def loadrescuetime():

    s = Service.Service()
    k = AnalyticApiKey.AnalyticApiKey(open('/home/alex/.rescuetime/rt_key').read(), s)
    p = {}

    p['restrict_begin'] = '2014-01-01'
    p['restrict_end'] = (datetime.date.today()+datetime.timedelta(1)).strftime("%Y-%m-%d")
    p['restrict_kind']  = 'efficiency'
    p['perspective']    = 'interval'
    p['resolution_time'] = 'day'
    d = s.fetch_data(k,p)

    df = pd.DataFrame(d['rows'], columns=d['row_headers'])
    df['Date'] = pd.to_datetime(df.Date)
    df['Date'] = df['Date']-np.timedelta64(0, 'D')
    df.set_index('Date',inplace=True)
    return df 

