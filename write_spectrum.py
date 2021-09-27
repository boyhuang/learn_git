from numpy import *
from os import listdir
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

print('Hello, world')

print('huang zhangtao')

print('xu jinlan')

print('we are together')

print('full in love')

print('debug test')

print('debug test2')

print('new feature1')

def file2matrix(filename):

    fr = open(filename)
    i = 0
    j = 0
    index = 0
    for line in fr.readlines():
        if index ==0:
            step = float(line)
        elif index == 1:
            start_x = float(line.split(' ')[0])
            num_x = int(line.split(' ')[1])
        elif index == 2:
            start_y = float(line.split(' ')[0])
            num_y = int(line.split(' ')[1])
            matrix = zeros((num_x,num_y))
        elif index > 2:
            line = line.strip()
            if line == '0':
                pass
            else:
                matrix[i,j] = (math.log(double(line)+1,10))
            i += 1
            if i == num_x:
                j += 1
                i = 0
        index += 1

    return step,start_x,num_x,start_y,num_y,matrix

def plot_spectrum(file):
    get_data = file2matrix(file)
    dataMat=get_data[5]
    step = get_data[0]
    start_x = get_data[1]
    num_x = get_data[2]
    end_x = start_x + step*num_x
    start_y = get_data[3]
    num_y = get_data[4]
    end_y = start_y + step*num_y

    x_axis = np.arange(start_x,end_x,step)
    y_axis = np.arange(start_y,end_y,step)
    X,Y=np.meshgrid(x_axis,y_axis)
    Z = dataMat
    figure = plt.figure()
    plt.pcolor(X,Y,Z,cmap='binary',shading='auto')
    plt.show()

file = r"C:\Users\zhang\Desktop\CT_P80.txt"
plot_spectrum(file)
