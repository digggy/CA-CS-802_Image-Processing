import math
import numpy as np

mask = -2
wshed = 0
init = -1
inqueue = -3
h_min = 1000, h_max = -1000
input_f = [] , output_f = []

line = None, flag = None, current_label = None, Ng_p = None
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
	current_label = 0;
	flag = false;

def sort_pixels():
    input_f = input_f.sort()

def watershed_transform():



if __name__ == main():
    watershed_transform()