from numpy import *
from os import listdir
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import argparse
import os
import matplotlib
from matplotlib.pyplot import MultipleLocator

print('hello world')

print('hello world2')

def file2matrix(filename):
    fr = open(filename)
    numberOfLines = len(fr.readlines())         #get the number of lines in the file
    returnMat = zeros((numberOfLines,3))        #prepare matrix to return
    classLabelVector = []                       #prepare labels return   
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
            matrix = zeros((num_y,num_x))
        elif index > 2:
            line = line.strip()
            if line == '0':
                pass
            else:
                matrix[j, i] = double(line)
            i += 1
            if i == num_x:
                j += 1
                i = 0
        index += 1

    return step,start_x,num_x,start_y,num_y,matrix

def get_colormap(src_mat):
    cwd = os.path.dirname(__file__)
    map_path = os.path.join(cwd, 'Color_MAP.csv')
    cm_mat = np.loadtxt(map_path)
    c_num = len(cm_mat)
    values = np.linspace(0, 1, c_num)
    reds = cm_mat[:, 0]
    greens = cm_mat[:, 1]
    blues = cm_mat[:, 2]
    rdata = np.column_stack((values, reds, reds))
    gdata = np.column_stack((values, greens, greens))
    bdata = np.column_stack((values, blues, blues))
    c_dict = {'red': rdata, 'green': gdata, 'blue': bdata}
    cmap = matplotlib.colors.LinearSegmentedColormap('Color_Map', c_dict)
    return cmap

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
    X, Y=np.meshgrid(x_axis,y_axis)
    Z = dataMat

    ext = (start_x, start_x + step * num_x, start_y, start_y + step * num_y)
    cmap = get_colormap(Z)
    cmap.set_bad('w')
    
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    x_major_locator = MultipleLocator(1)
    y_major_locator = MultipleLocator(1)
    ax.xaxis.set_major_locator(x_major_locator)
    ax.yaxis.set_major_locator(y_major_locator)

    #ax.set_ylabel('sy')
    #ax.set_xlabel('sx')
    plt.xlabel('sx', fontsize=18)
    plt.ylabel('sy', fontsize=18)
    plt.tick_params(labelsize=16)
    img = ax.imshow(Z, aspect='equal', origin='lower', extent=ext, cmap=cmap)
    
    plt.show()

if __name__ == '__main__':
    parse = argparse.ArgumentParser()
    parse.add_argument('C:\Users\zhang\Desktop', dest=r'C:\Users\zhang\Desktop', help= r'C:\Users\zhang\Desktop', required=True, default='')
    args = parse.parse_args()
    ms_file = args.ms_path
    plot_spectrum(ms_file)
