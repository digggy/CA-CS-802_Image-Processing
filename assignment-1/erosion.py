import numpy as np

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

    square_three_with_zero = np.array([[1,1,1],
                            [1,0,1],
                            [1,1,1]])

    f1_square_identical_indices = []
    f1_subarr = []
    f1_erosion = np.zeros((f1.shape[0], f1.shape[1]), int)

    
   
   # find sub-matrices inside the original matrix which are identical to the erosion matrix
    for i in range(f1.shape[0]):
        for j in range(f1.shape[1]):
            f1_subarr =  f1_with_boundary[i:i+3, j:j+3]
            if np.array_equal(f1_subarr, square_three_ones) or np.array_equal(f1_subarr, square_three_with_zero):
                f1_square_identical_indices.append((i,j))
    
    print(f1_square_identical_indices)
    
   
    
    # apply erosion result to the original array 
    for i in range(f1.shape[0]):
        for j in range(f1.shape[1]):
            if (i,j) in f1_square_identical_indices: 
                f1_erosion[i, j] = 1
    
    print(f1_erosion)


if __name__ == "__main__":
    erosion_f1()