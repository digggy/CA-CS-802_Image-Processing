import numpy as np
from matplotlib import pyplot as plt
from numpy import genfromtxt
plt.rcParams["figure.figsize"] = (25, 5)


def morph_operation(img, SE, operation_type):
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

