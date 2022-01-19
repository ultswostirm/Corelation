import csv
import numpy as np
import plotly_express as px

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig = px.scatter(df,x="Size of TV", y="Average time spent watching TV in a week (hours)")
        fig.show()

def getDataSource(data_path):
    Size = []
    AvgTime = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Size.append(float(row["Size of TV"]))
            AvgTime.append(float(row["Average time spent watching TV in a week (hours)"]))

    return {"x" : Size, "y": AvgTime}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Size of TV and Average time spent on watching tv in a week (hours) :-  \n--->",correlation[0,1])

def setup():
    data_path  = 'Tv.csv'

    datasource = getDataSource(data_path)
    findCorrelation(datasource)

    plotFigure(data_path)
setup()