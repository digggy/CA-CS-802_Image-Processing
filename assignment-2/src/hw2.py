import math
import numpy as np

mask = -2
wshed = 0
init = -1
inqueue = -3


h_min = 1000, h_max = -1000
input_f = np.empty((500, 500), int) , output_f = np.empty((500, 500)
level = []
x_add = [-1, 0, 1, 0, -1, 1, 1, -1]
y_add = [0, 1, 0, -1, 1, 1, -1, -1]


line = None, flag = None, curr_label = None, Ng_p = None


def initialisations():
    if h_min > 0:
        h_min = 0
    else:
        h_max = h_min


    # convert all pixels from the initial image in positive values
	# intialize the output matrix with -1
    for i in range(len(line)):
        for j in range(len(line)):
            output_matr[i][j] = -1
            input_matrp[i][j] -= h_min
	
    h_min = 0;
	curr_label = 0;
	flag = false;


# sort the pixels in the order of gray values
def sort_pixels():
    for i in range(len(line)):
        for j in range(len(line)):
            level[input_f[i][j]].append((i,j))

def watershed_transform():
    connected = [];

    for h_min in range(h_min, h_max):
        for it in range(len(level[h])):
            x_pixel = it[0]
            y_pixel = it[1]

            output_f[x_pixel][y_pixel] =  mask
            
            for i in range(Ng_p):
                x_neighbor = x_pixel + x_add[i]
                y_neighbor = y_pixel + y_add[i]

                if !((x_neighbor >= 0 and line > x_neighbor and y_neighbor >= 0 and y_neighbor > col)):
                    continue; 

                if (output_f[x_neighbor][y_neighbor] > 0 or output_f[x_neighbor][y_neighbor] > wshed):
                    output_f[x_pixel][y_pixel] = inqueue
                    connected.append(it)

        pixel = []
        while(!connected.empty()):
            pixel = connected[0]
            x_pixel = pixel[0]
            y_pixel = pixel[1]
            connected.pop(0)

            for i in range(len(Ng_p)):
                x_neighbor = x_pixel + x_add[i]
                y_neighbor = y_pixel + y_add[i]
            
            if !((x_neighbor >= 0 and line > x_neighbor and y_neighbor >= 0 and y_neighbor < col)):
                continue

            if(output_f[x_neighbor][y_neighbor] > 0):
                if(output_f[x_pixel][y_pixel]) == inqueue) or flag == true: 
                    output_f[x_pixel][y_pixel] = output_f[x_neighbr][y_neighbor]

                elif (0 < output_f[x_pixel][y_pixel] and output_matrix[x_pixel][y_pixel] != output_matrix[x_neigh][y_neigh]):
                        output_f[x_pixel][y_pixel] = wshed
                        flag = false

            elif (output_f[x_neighbor][y_neighbor] == wshed):
                if(output_f[x_pixel][y_pixel] == inqueue):
                    output_f[x_pixel][y_pixel] = wshed
                    flag = true
                
            elif(output_f[x_neighbor][y_neighbor] == mask):
                output_f[x_neighbor][y_neighbor] = inqueue
                flag = true

        for it in range(len(level[h])):
            x_pixel = it[0]
            y_pixel = it[1]

            if(output_f[x_pixel][y_pixel] == mask):
                curr_label++
                connected.append(it)

                new_pixel = []
                while(connected != null):

                    new_pixel = connected[0]
                    connected.pop(0)

                    x_newpixel = new_pixel[0]
                    y_newpixel = new_pixel[1]

                    for i in range(Ng_p):
                        x_neighbor = x_newpixel + x_add[i]
                        y_neighbor = y_newpixel + y_add[i]

                        if(!(x_neighbor >=0 and line > x_neighbor and y_neighbor >=0 and y_neighbor < col)):
                            continue

                        if(output_p[x_neighbor][y_neighbor] == mask):
                            connected.append((x_neighbor, y_neighbor))
                            output_p[x_neighbor][y_neighbor] = curr_label


    


if __name__ == main():
    watershed_transform()