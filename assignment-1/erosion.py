import numpy as np
import csv
from PIL import Image as im 
from matplotlib import pyplot as plt


def erosion_f1(): 
    f1 = np.array([[1, 1, 1, 1, 1], 
            [1, 0, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 0, 1, 1, 1],
            [1, 1, 1, 1, 1]])

    f1_with_boundary = np.ones((f1.shape[0]+2, f1.shape[1]+2))
    
    f1_with_boundary[1:f1.shape[0]+1, 1:f1.shape[1]+1] = f1
    # print(f1_with_boundary)
    square_three_ones = np.array([[1,1,1],
                            [1,1,1],
                            [1,1,1]])

    # square_three_with_zero = np.array([[1,1,1],
    #                         [1,0,1],
    #                         [1,1,1]])

    f1_square_identical_indices = []
    f1_subarr = []
    f1_erosion = np.zeros((f1.shape[0], f1.shape[1]), int)

    
   
   # find sub-matrices inside the original matrix which are identical to the erosion matrix
    for i in range(f1.shape[0]):
        for j in range(f1.shape[1]):
            f1_subarr =  f1_with_boundary[i:i+3, j:j+3]
            if np.array_equal(f1_subarr, square_three_ones):
                f1_square_identical_indices.append((i,j))
    
    print(f1_square_identical_indices)
    
    # apply erosion result to the original array 
    for i in range(f1.shape[0]):
        for j in range(f1.shape[1]):
            if (i,j) in f1_square_identical_indices: 
                f1_erosion[i, j] = 1
    
    print(f1_erosion)

def erosion_f2():
    f2 = np.array([[2, 4, 5, 5, 3],
                [1, 0, 5, 5, 5],
                [3, 2, 3, 4, 5],
                [1, 2, 3, 4, 0],
                [4, 4, 4, 4, 3]])

    vertical_SE = np.array([[1],[1], [1]])
    f2_with_boundary = np.ones((f2.shape[0]+2, f2.shape[1]))
    f2_with_boundary[1:f2.shape[0]+1, 0:f2.shape[1]] = f2
    f2_with_boundary[0, 0:f2.shape[1]] = np.array([np.inf, np.inf, np.inf, np.inf, np.inf])
    f2_with_boundary[f2.shape[0]+1, 0:f2.shape[1]] = np.array([np.inf, np.inf, np.inf, np.inf, np.inf])
    f2_erosion = np.zeros((f2.shape[0], f2.shape[1]), int)
    # print(f2_with_boundary)

    for i in range(f2.shape[0]):
        for j in range(f2.shape[1]):
            f2_subarr = f2_with_boundary[i:i+3, j]
            
            f2_erosion[i,j] = np.min(f2_subarr)

    print(f2_erosion)



def erosion_f3():

    f3_from_txt = []
    with open('f3.txt','r') as f1_csv:
        csv_reader = csv.reader(f1_csv)
        for line in csv_reader:
            f3_from_txt.append(list(map(int, line)))

    f3 = np.array(f3_from_txt)      
   
    f3_with_boundary = np.ones((f3.shape[0], f3.shape[1]+2))

    for i in range(f3.shape[0]):
        f3_with_boundary[i, 0] = np.inf
        f3_with_boundary[i, f3.shape[1]+1] = np.inf

    f3_with_boundary[0:f3.shape[0], 1:f3.shape[1]+1] = f3
    # print(f3_with_boundary)

    f3_erosion = np.zeros((f3.shape[0], f3.shape[1]), int)
    horizontal_SE = np.array([1,1,1])
    for i in range(f3.shape[0]):
        for j in range(f3.shape[1]):
            f3_subarr = f3_with_boundary[i, j:j+3]
            f3_erosion[i,j] = np.min(f3_subarr)
            
    print(f3_erosion)
    
    # img = im.fromarray(f3_erosion) 
    # img.save('f3-result.png').show() 

if __name__ == "__main__":
    erosion_f3()