import numpy as np
import  pandas as pd
from matplotlib import pyplot as plt
#ploting our canvas
plt.plot([1,2,3],[4,5,1])
#display the graph
plt.show()

def firstPlot():
    x = [5, 2, 7]
    y = [1, 10, 4]
    plt.plot(x, y)
    plt.title('Line graph')
    plt.ylabel('Y axis')
    plt.xlabel('X axis')
    plt.show()
for i in range(5):
    firstPlot()

def secondPlot():
    names = ['Abhishek', 'Himanshu', 'Devansh']
    marks = [87, 50, 98]

    plt.figure(figsize=(9, 3))

    plt.subplot(131)
    plt.bar(names, marks)
    plt.subplot(132)
    plt.scatter(names, marks)
    plt.subplot(133)
    plt.plot(names, marks)
    plt.suptitle('Categorical Plotting')
    plt.show()  

secondPlot()