import pandas as pd
import plotly.express as px
import csv


mean = 40
add = 403
length = 9

def mean():
    with open("marks.csv") as f:
        reader = csv.reader(f)
        data = list(reader)

    data.pop(0)
    add = 0
    for i in range(len(data)):
        #print(data[i][2])
        new_data = data[i][1]
        #print(new_data)
        New_Data = int(data[i][1])
        #print(New_Data)
        add += New_Data
        #print(add)

    length = len(data)
    print(length)
    print("")
    print("")
    mean = add/len(data)
    print("The average = ",mean)
    print("The total = ",add)



def scatter():
    df = pd.read_csv("marks.csv")
    fig = px.scatter(df, x='Section', y='Marks', title='Marks')
    fig.update_layout(shapes=[dict(
        type='line',
        y0=mean, y1=mean,
        x0=0, x1=length)])
    fig.show()

#mean()
scatter()
