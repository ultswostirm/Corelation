import csv
import numpy as np
import plotly_express as px
import pandas as pd

def plotFigure(data_path):
    df = pd.read_csv(data_path)
    fig = px.scatter(df,x="Coffee in ml", y="sleep in hours")
    fig.show()

def getDataSource(data_path):
    Coffee = []
    Sleep = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Coffee.append(float(row["Coffee in ml"]))
            Sleep.append(float(row["sleep in hours"]))

    return {"x" : Coffee, "y": Sleep}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Coffee and sleep in hours :-  \n--->",correlation[0,1])

def setup():
    data_path  = 'coffee.csv'

    datasource = getDataSource(data_path)
    findCorrelation(datasource)

    plotFigure(data_path)
setup()