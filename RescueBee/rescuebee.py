# This function loads up the required data
import pandas as pd
import matplotlib.pyplot as plt
import loadrescuetimedata
import numpy as np
def loaddata():
    """ 
    This function loads up RescueTime data
    and Beeminder Data
    """
    "Load Beeminder CSV"
    header_row = ['date', 'mg','comment', 'source']
    data_chew = pd.read_csv('chew.csv', header=None)
    data_chew.columns = header_row

    """ Load in RescueTime data """
    data_rescue = loadrescuetimedata.loadrescuetime()
    return data_chew, data_rescue

def visualise(t, x):
   plt.plot(t, x) 


if __name__ == "__main__":
    df_chew, df_rescue = loaddata()
    t = df_chew['date']
    x = df_chew['mg']
    pd.to_datetime(df_chew['date'])
    df_chew.set_index('date',inplace=True)
    merged = pd.merge(df_chew, df_rescue, left_index=True, right_index=True)
    """ Perform some basic linear regressions """
    regression = np.polyfit(df_rescue['Time Spent (seconds)']/60**2, df_rescue['Efficiency (percent)'],1)
    print regression



