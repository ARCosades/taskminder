# coding: utf-8
import pprint
import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
from rescuetime.api.service import Service
from rescuetime.api.access import AnalyticApiKey
 
s = Service.Service()
k = AnalyticApiKey.AnalyticApiKey(open('rt_key').read(), s)
p = {}

p['restrict_begin'] = '2014-01-01'
p['restrict_end'] = '2014-12-01'
p['restrict_kind']  = 'efficiency'
p['perspective']    = 'interval'
d = s.fetch_data(k,p)

df = pd.DataFrame(d['rows'], columns=d['row_headers'])
df['Date'] = pd.to_datetime(df.Date)
df.set_index('Date',inplace=True)

x = []
x = np.zeros([24,7])


for i in range(24,):
    dfi = df.at_time(datetime.time(i,0))['Efficiency (percent)']
    for j in range(7,):
        dfij = dfi[dfi.index.dayofweek==j]
        x[i,j] = np.mean(dfij)

x = np.nan_to_num(x)

plt.pcolor(x)
plt.xlabel('Day of Week')
plt.ylabel('Hour of Day')

plt.show()


