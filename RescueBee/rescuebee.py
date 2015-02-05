# This function loads up the required data
import pandas as pd
import matplotlib.pyplot as plt

def loaddata():
    """ 
    This function loads up RescueTime data
    and Beeminder Data
    """
    "Load Beeminder CSV"
    data = pd.read_csv('chew.csv', header=None)
    return data

    """ Load in RescueTime data


def visualise(t, x):
   plt.plot(t, x) 


if __name__ == "__main__":
    data = loaddata()
    t = data[0]
    x = data[1]
    data.plot(0,1)
    



