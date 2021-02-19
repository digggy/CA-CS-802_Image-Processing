import numpy as np
import csv
from PIL import Image as im 
from matplotlib import pyplot as plt

def read_f3_values(filename):
    f3_from_txt = []
    with open(filename,'r') as f1_csv:
        csv_reader = csv.reader(f1_csv)
        for line in csv_reader:
            f3_from_txt.append(list(map(int, line)))
    
    f3 = np.array(f3_from_txt)
    return f3


def dilation_f3_square_five():

    square_five_ones = np.ones((5,5), int)
    f3 = read_f3_values('f3.txt')

    f3_with_boundary = np.ones((f3.shape[0], f3.shape[1]+2))

    for i in range(f3.shape[0]):
        f3_with_boundary[i, 0] = 0
        f3_with_boundary[i, f3.shape[1]+1] = 0

    f3_with_boundary[0:f3.shape[0], 1:f3.shape[1]+1] = f3
    f3_dilation = np.zeros((f3.shape[0], f3.shape[1]), int)
    square_five_ones_SE = np.ones((5,5), int)


    for i in range(f3_with_boundary.shape[0]-5):
        for j in range(f3_with_boundary.shape[1]-5):
            f3_subarr = f3_with_boundary[i:i+5, j:j+5]
            f3_dilation[i,j] = np.max(f3_subarr)

    np.savetxt('df3_d3.txt', f3_dilation,
               delimiter=', ', newline='\n', fmt='%d')
    

def dilation_f3_backward_diagonal():

    backward_nine_SE = np.eye(9)
    f3 = read_f3_values('f3.txt')
    f3_with_boundary = np.zeros((f3.shape[0]+2, f3.shape[1]+2))

    f3_with_boundary.fill(0)
    f3_with_boundary[0:f3.shape[0], 1:f3.shape[1]+1] = f3
    f3_dilation = np.zeros((f3.shape[0], f3.shape[1]), int)

    for i in range(f3_with_boundary.shape[0]-9):
        for j in range(f3_with_boundary.shape[0]-9):
            f3_subarr = f3_with_boundary[i:i+backward_nine_SE.shape[0], j:j+backward_nine_SE.shape[1]]
            f3_dilation[i,j] = np.max(np.diagonal(f3_subarr))
    
    np.savetxt('df3_d4.txt', f3_dilation,
               delimiter=', ', newline='\n', fmt='%d')


def dilation_f3_forward_diagonal():
    
    forward_nine_SE = np.flip(np.eye(9), 1)
    
    f3 = read_f3_values('f3.txt')
    f3_with_boundary = np.zeros((f3.shape[0]+2, f3.shape[1]+2))

    f3_with_boundary.fill(0)
    f3_with_boundary[0:f3.shape[0], 1:f3.shape[1]+1] = f3
    f3_dilation = np.zeros((f3.shape[0], f3.shape[1]), int)

    for i in range(f3_with_boundary.shape[0]-9):
        for j in range(f3_with_boundary.shape[0]-9):
            f3_subarr = f3_with_boundary[i:i+forward_nine_SE.shape[0], j:j+forward_nine_SE.shape[1]]
            f3_dilation[i,j] = np.max(np.diagonal(f3_subarr))
    
    np.savetxt('df3_d5.txt', f3_dilation,
               delimiter=', ', newline='\n', fmt='%d')


def opening_f3_square_five():
    f3 = read_f3_values('ef3_e3.txt')

    f3_with_boundary = np.ones((f3.shape[0], f3.shape[1]+2))

    for i in range(f3.shape[0]):
        f3_with_boundary[i, 0] = 0
        f3_with_boundary[i, f3.shape[1]+1] = 0

    f3_with_boundary[0:f3.shape[0], 1:f3.shape[1]+1] = f3
    f3_dilation = np.zeros((f3.shape[0], f3.shape[1]), int)
    square_five_ones_SE = np.ones((5,5), int)


    for i in range(f3_with_boundary.shape[0]-5):
        for j in range(f3_with_boundary.shape[1]-5):
            f3_subarr = f3_with_boundary[i:i+5, j:j+5]
            f3_dilation[i,j] = np.max(f3_subarr)

    np.savetxt('of3_o3.txt',  f3_dilation,
               delimiter=', ', newline='\n', fmt='%d')


def opening_f3_backward_diagonal():

    f3 = read_f3_values('ef3_e4.txt')
    
    backward_nine_SE = np.eye(9)
    f3_with_boundary = np.zeros((f3.shape[0]+2, f3.shape[1]+2))

    f3_with_boundary.fill(0)
    f3_with_boundary[0:f3.shape[0], 1:f3.shape[1]+1] = f3
    f3_dilation = np.zeros((f3.shape[0], f3.shape[1]), int)

    for i in range(f3_with_boundary.shape[0]-9):
        for j in range(f3_with_boundary.shape[0]-9):
            f3_subarr = f3_with_boundary[i:i+backward_nine_SE.shape[0], j:j+backward_nine_SE.shape[1]]
            f3_dilation[i,j] = np.max(np.diagonal(f3_subarr))
    
    np.savetxt('of3_o4.txt', f3_dilation,
               delimiter=', ', newline='\n', fmt='%d')


if __name__ == "__main__":
    # opening_f3_square_five()
    opening_f3_backward_diagonal()