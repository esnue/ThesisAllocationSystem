import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("./data/streamlit_data.csv")
# to percentages
df.loc[:, df.columns != 'prof'] = df.loc[:, df.columns != 'prof']*100

# figure and axis
fig, ax = plt.subplots(1, figsize=(12, 10))

fields = df.columns[1:].tolist()
plt.barh(df.loc[df['prof']=='WEGRICH',].drop('prof', axis = 1).squeeze(), df.columns[1:])

for idx, name in enumerate(fields):
    ax.barh(df['prof'], df[name])
plt.show()