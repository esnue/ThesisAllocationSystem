import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import matplotlib.colors as mcolors

df = pd.read_csv("./data/train-label_wide.csv")

def prep_table(data):
  # Remove number and .txt from prof
  data['prof'] = data['prof'].str.replace('[0-9]', '').str.replace('\.txt', '').str.upper()

  # Isolate prof name + topic values
  data1 = pd.concat([data['prof'], data.iloc[:, 3:31]], axis = 1)

  # Average topic proportions per professor
  data2 = data1.groupby('prof').mean().reset_index()
  return(data2)

bardat = prep_table(df)

def plot_topic(topicname, data):
  data1 = data.sort_values(topicname)
  plt.rcParams["figure.figsize"] = [10,6]
  data1.plot(
    x = 'prof',
    kind = 'barh',
    stacked = True,
    title = 'Distribution of Professors in Topics',
    mark_right = True,
    cmap="tab20c")

  plot_topic('Topic0', bardat)

  def plot_prof(profname, data):
    data1 = data[(data.prof == profname)]
    data2 = data1.transpose().iloc[1:].reset_index()
    data2.columns = ['topics', 'values']
    data2 = data2.sort_values(by=['values'], ascending=False)

    topics = list(data2.iloc[:, 0])
    values = list(data2.iloc[:, 1])

    y_pos = list(reversed(np.arange(len(topics))))
    plt.rcParams["figure.figsize"] = [10, 6]

    # Create horizontal bars
    plt.barh(y_pos, values)

    # Create names on the x-axis
    plt.yticks(y_pos, topics)

    # Show graphic
    plt.show()
