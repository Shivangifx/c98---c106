import pandas as pd
import plotly.express as px
df = pd.read_csv("csv files/line_chart.csv")
fig = px.pie(df,values='Per capita income',names='Country')
fig.show()
#print(df)
