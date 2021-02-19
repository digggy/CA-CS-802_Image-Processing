import numpy as np
import csv
from PIL import Image as im 
from matplotlib import pyplot as plt

###################### f1 ###############################
def erosion_f1(): 
    f1 = np.array([[1, 1, 1, 1, 1], 
            [1, 0, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 0, 1, 1, 1],
            [1, 1, 1, 1, 1]])

    f1_with_boundary = np.ones((f1.shape[0]+2, f1.shape[1]+2))
    
    f1_with_boundary[1:f1.shape[0]+1, 1:f1.shape[1]+1] = f1
    
    square_three_ones = np.array([[1,1,1],
                            [1,1,1],
                            [1,1,1]])


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



###################### f2 ###############################
def erosion_f2():
    f2 = np.array([[2, 4, 5, 5, 3],
                [1, 0, 5, 5, 5],
                [3, 2, 3, 4, 5],
                [1, 2, 3, 4, 0],
                [4, 4, 4, 4, 3]])

    vertical_SE = np.array([[1],[1], [1]])
    f2_with_boundary = np.ones((f2.shape[0]+2, f2.shape[1]))
    f2_with_boundary[1:f2.shape[0]+1, 0:f2.shape[1]] = f2
    
    f2_with_boundary[0, 0:f2.shape[1]].fill(5)
    f2_with_boundary[f2.shape[0]+1, 0:f2.shape[1]].fill(np.max(f2))
    f2_erosion = np.zeros((f2.shape[0], f2.shape[1]), int)
    # print(f2_with_boundary)

    for i in range(f2.shape[0]):
        for j in range(f2.shape[1]):
            f2_subarr = f2_with_boundary[i:i+3, j]
            
            f2_erosion[i,j] = np.min(f2_subarr)

    print(f2_erosion)



###################### f3 ###############################
def read_f3_values():
    f3_from_txt = []
    with open('f3.txt','r') as f1_csv:
        csv_reader = csv.reader(f1_csv)
        for line in csv_reader:
            f3_from_txt.append(list(map(int, line)))
    
    f3 = np.array(f3_from_txt)
    return f3


def erosion_f3_horizontal():
    f3 = read_f3_values()
   
    f3_with_boundary = np.ones((f3.shape[0], f3.shape[1]+2))

    for i in range(f3.shape[0]):
        f3_with_boundary[i, 0] = 255
        f3_with_boundary[i, f3.shape[1]+1] = 255

    f3_with_boundary[0:f3.shape[0], 1:f3.shape[1]+1] = f3
    # print(f3_with_boundary)

    f3_erosion = np.zeros((f3.shape[0], f3.shape[1]), int)
    horizontal_SE = np.array([1,1,1])
    for i in range(f3.shape[0]):
        for j in range(f3.shape[1]):
            f3_subarr = f3_with_boundary[i, j:j+3]
            f3_erosion[i,j] = np.min(f3_subarr)

    np.savetxt('ef3_e2.txt', f3_erosion,
               delimiter=', ', newline='\n', fmt='%d')



def erosion_f3_square_five():

    square_five_ones = np.ones((5,5), int)
    f3 = read_f3_values()

    f3_with_boundary = np.ones((f3.shape[0], f3.shape[1]+2))

    for i in range(f3.shape[0]):
        f3_with_boundary[i, 0] = 255
        f3_with_boundary[i, f3.shape[1]+1] = 255

    f3_with_boundary[0:f3.shape[0], 1:f3.shape[1]+1] = f3
    f3_erosion = np.zeros((f3.shape[0], f3.shape[1]), int)
    square_five_ones_SE = np.ones((5,5), int)


    for i in range(f3_with_boundary.shape[0]-5):
        for j in range(f3_with_boundary.shape[1]-5):
            f3_subarr = f3_with_boundary[i:i+5, j:j+5]
            
            f3_erosion[i,j] = np.min(f3_subarr)

    np.savetxt('ef3_e3.txt', f3_erosion,
               delimiter=', ', newline='\n', fmt='%d')
    

def erosion_f3_backward_diagonal():

    backward_nine_SE = np.eye(9)
    f3 = read_f3_values()
    f3_with_boundary = np.zeros((f3.shape[0]+2, f3.shape[1]+2))

    f3_with_boundary.fill(255)
    f3_with_boundary[0:f3.shape[0], 1:f3.shape[1]+1] = f3
    f3_erosion = np.zeros((f3.shape[0], f3.shape[1]), int)

    for i in range(f3_with_boundary.shape[0]-9):
        for j in range(f3_with_boundary.shape[0]-9):
            f3_subarr = f3_with_boundary[i:i+backward_nine_SE.shape[0], j:j+backward_nine_SE.shape[1]]
            f3_erosion[i,j] = np.min(np.diagonal(f3_subarr))
    
    np.savetxt('ef3_e4.txt', f3_erosion,
               delimiter=', ', newline='\n', fmt='%d')

def erosion_f3_forward_diagonal():
    
    forward_nine_SE = np.flip(np.eye(9), 1)
    
    f3 = read_f3_values()
    f3_with_boundary = np.zeros((f3.shape[0]+2, f3.shape[1]+2))

    f3_with_boundary.fill(255)
    f3_with_boundary[0:f3.shape[0], 1:f3.shape[1]+1] = f3
    f3_erosion = np.zeros((f3.shape[0], f3.shape[1]), int)

    for i in range(f3_with_boundary.shape[0]-9):
        for j in range(f3_with_boundary.shape[0]-9):
            f3_subarr = f3_with_boundary[i:i+forward_nine_SE.shape[0], j:j+forward_nine_SE.shape[1]]
            f3_erosion[i,j] = np.min(np.diagonal(f3_subarr))
    
    np.savetxt('ef3_e5.txt', f3_erosion,
               delimiter=', ', newline='\n', fmt='%d')

if __name__ == "__main__":
    erosion_f3_horizontal()