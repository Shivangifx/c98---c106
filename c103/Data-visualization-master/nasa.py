import pandas as pd
import plotly.express as px
df = pd.read_csv("csv files/nasa.csv")
fig = px.histogram(df,x = 'Year',y = 'Anomaly',color = 'Actual Temp',title = 'Global Land and Ocean Temperature Anomalies')
fig.show()
#print(df)
