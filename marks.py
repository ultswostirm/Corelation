import csv
import numpy as np
import plotly_express as px
import pandas as pd

def plotFigure(data_path):
    df = pd.read_csv(data_path)
    fig = px.scatter(df,x="Marks In Percentage", y="Days Present")
    fig.show()

def getDataSource(data_path):
    Marks = []
    Day = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Marks.append(float(row["Marks In Percentage"]))
            Day.append(float(row["Days Present"]))

    return {"x" : Marks, "y": Day}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Marks and Days Present:-  \n--->",correlation[0,1])

def setup():
    data_path  = 'marks.csv'

    datasource = getDataSource(data_path)
    findCorrelation(datasource)

    plotFigure(data_path)
setup()