#Linear Regression code by Vikram Shenoy
from random import randint
import numpy as np

from plotly import tools
import plotly.plotly as py
import plotly.graph_objs as go

#File Updater Code
def updateDataFile():
    file = open("data.txt", "w")
    file.close()
    file = open("data.txt", "w")
    for i in range(0,50):
        if ( i == 0 ):
            file.write(str(randint(60, 99)) + " " + str(randint(60, 99)))
        else:
            file.write("\n" + str(randint(60, 99)) + " " + str(randint(60, 99)))
    file.close()
    return

#Extract Data From A File
def extractDataFromFile():
    x_input = []
    y_input = []
    split = []
    file = open("data.txt", "r")
    n = 0
    for line in file:
        split = line.split(' ')
        x_input.append(split[0])
        y_input.append(split[1])
        n = n + 1
    file.close()
    x_IV = (np.array(x_input)).astype(float)
    y_DV = (np.array(y_input)).astype(float)
    return (x_IV,y_DV,n)

#Calculate Linear Regression
def linearRegression(x_IV,y_DV,n):
    meanX = 0
    meanY = 0
    Num = 0
    Den = 0

    for i in range(0, n):
        meanX = float(meanX + x_IV[i])
    meanX = float(meanX / n)

    for i in range(0,n):
        meanY = float(meanY + y_DV[i])
    meanY = float(meanY/n)

    for i in range(0,n):
        Num  = Num + float((x_IV[i] - meanX) * (y_DV[i] - meanY))
        Den = Den + float((x_IV[i] - meanX) ** 2)

    m = float(Num/Den)
    c = float(meanY - float(m * meanX))
    print "Slope = %f \ny-intercept = %f \n" % (m,c)
    return m,c

#Predict Dependent Variable
def predictDependentVariable():
    print "Enter the value of Independent Variable x :"
    x_new = float(raw_input())
    y_new = float((m * x_new) + c)

    print "The predicted value of Dependent Variable y is"
    print "%f" % (y_new)
    return

def drawGraph(x_axis, y_axis, m, c):
    py.sign_in('VikramShenoy','x1Un4yD3HDRT838vRkFA')

    trace0 = go.Scatter(
    x = x_axis,
    y = y_axis,
    mode = "markers",
    name = "Data"
    )

    x_1 = min(x_axis)-20
    x_2 = max(x_axis)+20
    y_1 = m*x_1 + c
    y_2 = m*x_2 + c

    trace1 = go.Scatter(
    x = [x_1, x_2],
    y = [y_1, y_2],
    mode = "lines",
    name = "Regression Line"
    )
    data = go.Data([trace0, trace1])
    layout = go.Layout()
    fig = go.Figure(data=data, layout=layout)
    fig['layout']['yaxis1'].update(title="Dependent Variable",range= [min(y_axis)-20,max(y_axis)+10], showline = True)
    fig['layout']['xaxis1'].update(title="Independent Variable", range= [min(x_axis)-20,max(x_axis)+10], showline = True)
    py.image.save_as(fig, filename="Graph.png")
    print "Graph Created"


#Remove the '#' of updateDataFile() below to change the dataset automatically
#updateDataFile()
x_IV, y_DV, n = extractDataFromFile()
m, c = linearRegression(x_IV,y_DV,n)
predictDependentVariable()
y = float((m * max(x_IV)) + c)
drawGraph(x_IV, y_DV, m, c)
