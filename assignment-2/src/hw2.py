import math
import numpy as np
from numpy import genfromtxt
import matplotlib.pyplot as plt
import watershed

mask = -2
wshed = 0
init = -1
inqueue = -3


h_min = 1000
h_max = -1000
input_f = []
output_f = []
level = []
x_add = [-1, 0, 1, 0, -1, 1, 1, -1]
y_add = [0, 1, 0, -1, 1, 1, -1, -1]


line = 0
flag = False
curr_label = 0



def initialisations(input_f):
    global h_min, h_max, curr_label, flag, line
    line = len(input_f)
    # for i in range(line):
    #     for j in range(line):
    #         if (input_f[i][j] < h_min):
    #             h_min = input_f[i, j]
    #         if (input_f[i,j] > h_max):
    #             h_max = input_f[i, j]

   
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
            input_f[i, j] -= h_min
	
    h_min = 0
    curr_label = 0
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

def watershed_transform(input_f, output_f, level, Ng_p):
    
    connected = []
    col = len(input_f[0])
    h_min = np.min(input_f)
    h_max = np.max(input_f)
    global curr_label, wshed, mask, inqueue, flag
   

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
                    connected.append(level[h][it])

        
        pixel = []
        while(len(connected) > 0):
            
            pixel = connected[0]
            x_pixel = pixel[0]
            y_pixel = pixel[1]
            connected.pop(0)
            
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
                    connected.append((x_neighbor, y_neighbor))


        for it in range(len(level[h])):
            x_pixel = level[h][it][0]
            y_pixel = level[h][it][1]
            if(output_f[x_pixel, y_pixel] == mask):
              
                curr_label += 1
                connected.append(level[h][it])
                output_f[x_pixel, y_pixel] = curr_label

                new_pixel = []

                while(len(connected) > 0):
                    new_pixel = connected[0]
                    connected.pop(0)
                    
                    x_newpixel = new_pixel[0]
                    y_newpixel = new_pixel[1]

                    for i in range(Ng_p):
                        x_neighbor = x_newpixel + x_add[i]
                        y_neighbor = y_newpixel + y_add[i]
                        

                        if(not (x_neighbor >=0 and  x_neighbor < line and y_neighbor >=0 and y_neighbor < col)):
                            continue

                        if(output_f[x_neighbor, y_neighbor] == mask):
                            connected.append([x_neighbor, y_neighbor])
                            output_f[x_neighbor, y_neighbor] = curr_label
    
    return output_f

    

def main(): 
    # initialisation(input)
    image = genfromtxt('../input/f2.txt',  delimiter=',').astype(int)
    old_min= np.min(image)
    image -= old_min   
    input_f, output_f = initialisations(image)
    sorted_bucket = sort_pixels(input_f)
    Ng_p = 4
    result = watershed_transform(input_f, output_f, sorted_bucket, Ng_p)
    # print(result/np.max(result))
    print("With " , Ng_p, "connected neighbors: ")
    print(result)
    plt.imshow(result, cmap='gray', vmin=0, vmax=255)
    plt.show()
    

if __name__ == main():
    main()