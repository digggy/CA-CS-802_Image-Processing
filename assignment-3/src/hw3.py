import math
import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt
import time

import argparse
import os.path
from skimage import color, io, data
from skimage.color import rgb2gray

bin_size = 0
histo_dim = 0
histo_1d = np.zeros((2,256))
histo_2d = np.zeros((256,256))
width = 0
height = 0
channel = np.zeros((2,1500, 1500))


def init():
    global bin_size, histo_dim
    histo_dim = int(256 / bin_size + 1)


def histogram_1d(idx, x_start, x_end, y_start, y_end):

    global histo_1d, bin_size, histo_dim, channel
    counter = np.zeros(256)
    for x in range(x_start, x_end-1):
        for y in range(y_start, y_end-1):
            index = int(channel[idx][x][y] / bin_size)
            counter[index] += 1
            # print(channel[idx][x][y], index)

    dim = (x_end - x_start) * (y_end - y_start)
    histo_1d[idx, :] = counter / dim
    

def histogram_2d(shift):

    global histo_2d, bin_size, width, height, channel
    counter = np.zeros((256, 256))
    
    histogram_1d(0,0,width, 0, height)
    histogram_1d(1,0,width, 0, height-40+shift)

    for i in range(width):
        for j in range(height):
            count_i = int(channel[0][i][j] / bin_size)
            count_j = int(channel[1][i][j+ shift] / bin_size)  
            counter[count_i][count_j] += 1
    
    dim = width * height
    histo_2d = counter / dim
    # for i in range(histo_dim):
    #     for j in range(histo_dim):
    #         histo_2d[i][j] = counter[i][j] / dim
            # print(histo_2d[i][j])

def mutual_information():
    global histo_1d, histo_2d, width, height, channel
    value = np.zeros(41)
    
    for shift in range(41):
        histo_1d = np.empty((2,256))
        histo_2d = np.empty((256,256))
        histogram_1d(0,0,width - 1, 0, height)
        histogram_1d(1,0,width, shift, height-40+shift)
        histogram_2d(shift)

        for y in range(histo_dim):
            for x in range(histo_dim):
                if (histo_1d[0][x] * histo_1d[1][y] > 0):
                    val = histo_2d[x][y] / histo_1d[0][x] * histo_1d[1][y]
                    if val > 0.0:
                        log_result = math.log10(float(val))
                        if(log_result > 0):
                            value[shift] += (histo_2d[x][y] * log_result)
                            print(value[shift])
                else:
                    continue

    return value


def main():

    input_img = io.imread("../input/f1_color.jpg")
    green_img = input_img[:,:,1]
    red_img = input_img[:,:,2]

    # plt.imshow(green_img)
    # plt.show()

    # plt.imshow(red_img)
    # plt.show()

    global width, height
    width = green_img.shape[1]
    height = green_img.shape[0]
    print(width, height)
    
    global bin_size, channel
    bin_size = 5

    green_img_trans = np.transpose(green_img)
    red_img_trans = np.transpose(red_img)
    channel[0,:width,:height] = green_img_trans
    channel[1,:width,:height] = red_img_trans

    init()
    result = mutual_information()
    print(result)
    np.savetxt("test.txt",result )


if __name__ == main():
    main()