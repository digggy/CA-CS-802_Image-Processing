import math
import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt
import time

import argparse
import os.path
from skimage import color, io, data
from skimage.color import rgb2gray


# declaration of constant values and neighbor ranges
mask = -2
wshed = 0
init = -1
inqueue = -3


h_min = 1000
h_max = -1000
level = []
x_add = [-1, 0, 1, 0, -1, 1, 1, -1]
y_add = [0, 1, 0, -1, 1, 1, -1, -1]


row = 0
col = 0
flag = False
cluster = 0


# 3
# initialise the output image numpy
def initialisations(input_f):

    global h_min, h_max, cluster, flag
    row = len(input_f)
    col = len(input_f[0])

    if h_min > 0:
        h_min = 0
    else:
        h_max -= h_min

    output_f = np.zeros(shape=(row, col))

    # convert all pixels from the initial image in positive values
    # intialize the output matrix with init
    for i in range(row):
        for j in range(col):
            output_f[i, j] = init

    h_min = 0
    cluster = 0
    flag = False

    return input_f, output_f

###############################################################
# sort the pixels in the order of gray values in a nested lislt
# put the pixels with the same gray value in the same list index


def sort_pixels(input_f):

    level = [[] for i in range(np.max(input_f)+1)]
    for i in range(len(input_f)):
        for j in range(len(input_f[0])):
            level[input_f[i, j]].append([i, j])

    return level


##############################
# Actuall Watershed algorithm
def watershed_transform(input_f, output_f, level, Ng_p):

    fifo = []
    row = len(input_f)
    col = len(input_f[0])
    h_min = np.min(input_f)
    h_max = np.max(input_f)
    global cluster, wshed, mask, inqueue, flag

    for h in range(h_min, h_max+1):
        for it in range(len(level[h])):
            x_pixel = level[h][it][0]
            y_pixel = level[h][it][1]

            output_f[x_pixel, y_pixel] = mask

            for i in range(Ng_p):
                x_neighbor = x_pixel + x_add[i]
                y_neighbor = y_pixel + y_add[i]

                if (not (x_neighbor >= 0 and x_neighbor < row and y_neighbor >= 0 and y_neighbor < col)):
                    continue

                if (output_f[x_neighbor, y_neighbor] > 0 or output_f[x_neighbor, y_neighbor] == wshed):
                    output_f[x_pixel, y_pixel] = inqueue
                    fifo.append(level[h][it])

        pixel = []
        while(len(fifo) > 0):

            pixel = fifo[0]
            x_pixel = pixel[0]
            y_pixel = pixel[1]
            fifo.pop(0)

            for i in range(Ng_p):
                x_neighbor = x_pixel + x_add[i]
                y_neighbor = y_pixel + y_add[i]

                if (not(x_neighbor >= 0 and x_neighbor < row and y_neighbor >= 0 and y_neighbor < col)):
                    continue

                if(output_f[x_neighbor, y_neighbor] > 0):
                    if((output_f[x_pixel, y_pixel] == inqueue) or (output_f[x_pixel, y_pixel] == wshed and flag == True)):
                        output_f[x_pixel,
                                 y_pixel] = output_f[x_neighbor, y_neighbor]

                    elif (output_f[x_pixel, y_pixel] > 0 and output_f[x_pixel, y_pixel] != output_f[x_neighbor, y_neighbor]):
                        output_f[x_pixel, y_pixel] = wshed
                        flag = False

                elif (output_f[x_neighbor, y_neighbor] == wshed):
                    if(output_f[x_pixel, y_pixel] == inqueue):
                        output_f[x_pixel, y_pixel] = wshed
                        flag = True

                elif(output_f[x_neighbor, y_neighbor] == mask):
                    output_f[x_neighbor, y_neighbor] = inqueue
                    fifo.append((x_neighbor, y_neighbor))

        for it in range(len(level[h])):
            x_pixel = level[h][it][0]
            y_pixel = level[h][it][1]
            if(output_f[x_pixel, y_pixel] == mask):

                cluster += 1
                fifo.append(level[h][it])
                output_f[x_pixel, y_pixel] = cluster

                new_pixel = []

                while(len(fifo) > 0):
                    new_pixel = fifo[0]
                    fifo.pop(0)

                    x_newpixel = new_pixel[0]
                    y_newpixel = new_pixel[1]

                    for i in range(Ng_p):
                        x_neighbor = x_newpixel + x_add[i]
                        y_neighbor = y_newpixel + y_add[i]

                        if(not (x_neighbor >= 0 and x_neighbor < row and y_neighbor >= 0 and y_neighbor < col)):
                            continue

                        if(output_f[x_neighbor, y_neighbor] == mask):
                            fifo.append([x_neighbor, y_neighbor])
                            output_f[x_neighbor, y_neighbor] = cluster

    return output_f


def erosion_dilation(img, SE, operation_type):
    # if(direction == "vertical"):
    #     SE = SE.reshape(SE.shape[0], 1)
    # elif(direction == "horizontal"):
    #     SE = SE.reshape(1, SE.shape[0])

    vmax = np.max(img)
    vmin = np.min(img)

    padding_value = None
    operation_dilation = None
    operation_erosion = None

    # operation type either dilation or erosion
    if(operation_type == 'd'):
        padding_value = vmin
        operation_dilation = True
    elif(operation_type == 'e'):
        padding_value = vmax
        operation_erosion = True

    SE_y = SE.shape[0]
    SE_x = SE.shape[1]

    # A flag for axes
    turn_off_axes = False
    if (img.shape[0] > 10 or img.shape[1] > 10):
        turn_off_axes = True

    padding_y, padding_x = SE.shape[0]//2, SE.shape[1]//2
    img_with_boundary = np.pad(img, ((padding_y, padding_y), (padding_x, padding_x)), mode='constant',
                               constant_values=padding_value)
    img_subarr = []

    img_output = np.zeros((img.shape[0], img.shape[1]), int)

    # get the idx of the 1s in the SE
    SE_one_idxs = np.argwhere(SE == 1)
    # find sub-matrices inside the original matrix which are identical to the erosion matrix
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img_subarr = img_with_boundary[i:i+SE_y, j:j+SE_x]
            img_subarr_filtered = []
            # iterate through the idxes 1s in the masking SE elements
            for one_idx in SE_one_idxs:
                img_subarr_filtered.append(img_subarr[one_idx[0], one_idx[1]])
            if (operation_erosion):
                img_output[i, j] = np.amin(img_subarr_filtered)
            elif(operation_dilation):
                img_output[i, j] = np.amax(img_subarr_filtered)
    return img_output

# global for filtering
BALANCE_ALPHA = 0.2

def get_median(filter_area):
    res = np.median(filter_area)
    return res

def median_filter(image, height, width):
    for row in range(1, height + 1):
        for column in range(1, width + 1):
            # 3 x 3 kernel
            filter_area = image[row - 1:row + 2, column - 1:column + 2]
            image[row][column] = get_median(filter_area)
    return image

def get_kernel():
    return np.ones((3, 3), np.float32) / 9


def get_mean_with_kernel(filter_area, kernel):
    return np.sum(np.multiply(kernel, filter_area))

def mean_filter(image, height, width):
    # Set the kernel.
    kernel = get_kernel()

    for row in range(1, height + 1):
        for column in range(1, width + 1):
            # Get the area to be filtered with range indexing.
            filter_area = image[row - 1:row + 2, column - 1:column + 2]
            res = get_mean_with_kernel(filter_area, kernel)
            image[row][column] = res

    return image

def mean_median_balanced_filter(image, height, width):
    for row in range(1, height + 1):
        for column in range(1, width + 1):
            filter_area = image[row - 1:row + 2, column - 1:column + 2]
            mean_filter_vector = get_mean_with_kernel(filter_area, get_kernel())
            median_filter_vector = get_median(filter_area)
            image[row][column] = BALANCE_ALPHA * mean_filter_vector + (1 - BALANCE_ALPHA) * median_filter_vector
    return image

def filter_image(image, image_name, filter_name, filtering_function):
    # Get the image size for the kernel looping.
    height, width = image.shape[:2]
    # Add 1px reflected padding to allow kernels to work properly.
    image = np.pad(image, 1, mode='edge')
    print("Calculating %s for %s" % (filter_name, image_name))
    start_time = time.time()
    res = filtering_function(image, height, width)
    print("Successfully calculated %s for %s in %s seconds." %
          (filter_name, image_name, str(time.time() - start_time)))
    return res

def main():

    my_parser = argparse.ArgumentParser(description='Perform watershed')

    my_parser.add_argument(
        '-i',
        '--input',
        dest="input",
        metavar='PATH',
        type=str,
        help='the path to input file')

    my_parser.add_argument(
        '-n'
        "--neighbors",
        dest="neighbors",
        metavar='N',
        type=int,
        help='number of neighbors')

    my_parser.add_argument(
        '-f'
        "--filter",
        dest="filter",
        choices=['median', 'balanced'],
        metavar='FILTER',
        type=str,
        help='name of filter')

    my_parser.add_argument(
        '-o'
        '--output',
        dest='output',
        metavar='PATH',
        type=str,
        help='the path to outputfile')

    args = my_parser.parse_args()
    image = None
    
    inputfile = args.input
    outputfile = args.output
    Ng_p = args.neighbors
    filter_selected = args.filter
    image_name = os.path.splitext(inputfile)[0]
    # check if the file is valid
    if inputfile and os.path.isfile(inputfile):
        input_image_extension = os.path.splitext(inputfile)[1]

        if(input_image_extension == ".png" or input_image_extension == ".jpg" or input_image_extension == ".jpeg"):
            # Image grascale intensity is set in the range 0 to 255
            image = io.imread(inputfile, as_gray=True)
            image -= np.min(image)
            image = image.astype(np.uint8)
        elif (input_image_extension == ".txt"):
            # Image grascale intensity is set in the range 0 to 1
            image = genfromtxt(inputfile, delimiter=',').astype(int)
            image -= np.min(image)

    else:
        print("Your input file doesnt have a valid path.")

    # SE = np.eye(5)

    if (filter_selected == "median"):
        image = filter_image(image, image_name, 'median filter', median_filter)
    elif (filter_selected == "balanced"):
        image = filter_image(image, image_name, 'median filter', mean_median_balanced_filter)
    
    input_f, output_f = initialisations(image)
    sorted_bucket = sort_pixels(input_f)
    img_output = watershed_transform(input_f, output_f, sorted_bucket, Ng_p)
    np.savetxt(outputfile, img_output, delimiter=', ', newline='\n', fmt='%d')

    plt.imshow(img_output, cmap='gray', vmin=0, vmax=np.max(img_output))
    plt.show()
    # plt.close()


if __name__ == main():
    main()
