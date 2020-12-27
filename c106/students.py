import pandas as pd
import plotly.express as px
df = pd.read_csv("students.csv")
fig = px.scatter(df,x = 'Temperature',y = 'Ice-cream Sales( ₹ )',title = 'ice cream v temp',)
fig.show()
