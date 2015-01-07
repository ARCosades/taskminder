# coding: utf-8
import pprint
import pandas as pd
import datetime
import time
import numpy as np
import matplotlib.pyplot as plt
from rescuetime.api.service import Service
from rescuetime.api.access import AnalyticApiKey

# Function for use later
def daterange(start_date, end_date):
        for n in range(int ((end_date - start_date).days)):
                    yield start_date + datetime.timedelta(n)

def hourssinceawake(TOD, awake):
    #    x = []
    #    for i in TOD:
    #        x.append(i+(24-awake) if i<awake else i-4)
    return TOD
     #   return np.array(x)



    

s = Service.Service()
k = AnalyticApiKey.AnalyticApiKey(open('/home/alex/.rescuetime/rt_key').read(), s)
p = {}

p['restrict_begin'] = '2014-01-01'
p['restrict_end'] = (datetime.date.today()+datetime.timedelta(1)).strftime("%Y-%m-%d")
p['restrict_kind']  = 'efficiency'
p['perspective']    = 'interval'
d = s.fetch_data(k,p)

df = pd.DataFrame(d['rows'], columns=d['row_headers'])
df['Date'] = pd.to_datetime(df.Date)
df['Date'] = df['Date']-np.timedelta64(4, 'h')
df.set_index('Date',inplace=True)
df['Waking Time (seconds)'] = hourssinceawake(df.index.hour,0)*60*60
x = np.zeros([24,7])

dfi_list = []

for i in range(24,):
    dfi = ((df['Efficiency (percent)']/100.0) * df['Time Spent (seconds)']).at_time(datetime.time(i,0))
    d
    dfi_list.append(dfi)
    for j in range(7,):
        dfij = dfi[dfi.index.dayofweek==j]
        x[i,j] = np.mean(dfij)

x = np.nan_to_num(x)

# Calculate efficiency as amount of work done by duration of work Day
start = datetime.datetime.strptime(p['restrict_begin'],"%Y-%m-%d")
end = datetime.datetime.strptime(p['restrict_end'],"%Y-%m-%d")
# For each day, calculate the cumulative productive hours worked

datelist = []

for date in daterange(start, end):
    datelist.append(date)


eff = []


for idx, date in enumerate(datelist):
    try:
        dfd = df[datelist[idx].strftime("%Y-%m-%d")]
        data = np.cumsum((dfd['Efficiency (percent)']/100.0)*dfd['Time Spent (seconds)'])/dfd['Waking Time (seconds)']
        eff.append(data)
    except Exception as inst:
        print "Failed on" + str(idx)

df2 = pd.concat(eff)
# Plot this efficiency percentile graph
plt.figure()
plt.scatter(x=hourssinceawake(df2.index.hour,0), y=df2)
# Highlight the last day
plt.scatter(x=hourssinceawake(eff[-1].index.hour,0), y=eff[-1], color='red')
plt.scatter(x=hourssinceawake(eff[-2].index.hour,0), y=eff[-2], color='green')
plt.show()




# Create a 24x7 heatmap of productivity
plt.figure()
plt.pcolor(x)
plt.xlabel('Day of Week')
plt.ylabel('Hour of Day')


# Create a scatter plot of efficiencies over time
plt.figure()
for idx, dfi_item in enumerate(dfi_list):
        plt.scatter(x=idx*np.ones(dfi_item.shape), y=dfi_item)


plt.show()




