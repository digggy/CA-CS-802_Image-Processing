import math
import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt

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


line = 0
flag = False
cluster = 0



def initialisations(input_f):
    global h_min, h_max, cluster, flag, line
    line = len(input_f)

    if h_min > 0:
        h_min = 0
    else:
        h_max -= h_min

    output_f = np.zeros(shape=(line, line))

    # convert all pixels from the initial image in positive values
	# intialize the output matrix with init
    for i in range(line):
        for j in range(line):
            output_f[i,j] = init
	
    h_min = 0
    cluster = 0
    flag = False

    return input_f, output_f


# # sort the pixels in the order of gray values
# # put the pixels with the same value in the same vector
def sort_pixels(input_f):

    level = [[] for i in range(np.max(input_f)+1)]
    for i in range(len(input_f)):
        for j in range(len(input_f[0])):
            level[input_f[i,j]].append([i,j])

    return level


##############################
## Actuall Watershed algorithm
def watershed_transform(input_f, output_f, level, Ng_p):
    
    fifo = []
    col = len(input_f[0])
    h_min = np.min(input_f)
    h_max = np.max(input_f)
    global cluster, wshed, mask, inqueue, flag
   

    for h in range(h_min, h_max+1):
        for it in range(len(level[h])):
            x_pixel = level[h][it][0]
            y_pixel = level[h][it][1]
    
            output_f[x_pixel, y_pixel] =  mask
            
            for i in range(Ng_p):
                x_neighbor = x_pixel + x_add[i]
                y_neighbor = y_pixel + y_add[i]
                    
                if (not (x_neighbor >= 0 and x_neighbor < line and y_neighbor >= 0 and y_neighbor < col)):
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
                
                if (not(x_neighbor >= 0 and x_neighbor < line and y_neighbor >= 0 and y_neighbor < col)):
                    continue

                if(output_f[x_neighbor, y_neighbor] > 0):
                    if((output_f[x_pixel, y_pixel] == inqueue) or (output_f[x_pixel, y_pixel] == wshed and flag == True)): 
                        output_f[x_pixel, y_pixel] = output_f[x_neighbor, y_neighbor]

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
                        

                        if(not (x_neighbor >=0 and  x_neighbor < line and y_neighbor >=0 and y_neighbor < col)):
                            continue

                        if(output_f[x_neighbor, y_neighbor] == mask):
                            fifo.append([x_neighbor, y_neighbor])
                            output_f[x_neighbor, y_neighbor] = cluster
    
    return output_f

    

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
        '--neighbors',
        dest="neighbors",
        metavar='N',
        type=int,
        help='number of neighbors')
    
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
    #check if the file is valid 
    if inputfile and os.path.isfile(inputfile):
        input_image_extension = os.path.splitext(inputfile)[1]
        
        if(input_image_extension == ".png" or input_image_extension == ".jpg" or input_image_extension == ".jgeg"):
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


    
    # image = genfromtxt('../input/f2.txt',  delimiter=',').astype(int)
    
    input_f, output_f = initialisations(image)
    sorted_bucket = sort_pixels(input_f)
    img_output = watershed_transform(input_f, output_f, sorted_bucket, Ng_p)
    np.savetxt(outputfile, img_output,
               delimiter=', ', newline='\n', fmt='%d')

    plt.imshow(img_output, cmap='gray', vmin=0, vmax=np.max(img_output))
    plt.show()
    # plt.close()
    
    

if __name__ == main():
    main()