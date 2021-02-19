import numpy as np
from matplotlib import pyplot as plt
from numpy import genfromtxt
plt.rcParams["figure.figsize"] = (25, 5)


def erosion():
    # Question 1
    img = genfromtxt('f1.txt', delimiter=',').astype(int)
    SE = genfromtxt('SE1.txt', delimiter=',').astype(int)


# Question 2
#     img=genfromtxt('f2.txt', delimiter=',').astype(int)
#     SE = genfromtxt('SE2.txt', delimiter=',').astype(int)
#     SE= SE.reshape(SE.shape[0],1)


# Question 3
# turn off the axis and gril lines to remove the blue lines in the boder
# check the diff between images to find the difference between eroded and original
#     img=genfromtxt('f3.txt', delimiter=',').astype(int)
#     SE = genfromtxt('SE3.txt', delimiter=',').astype(int)
#     SE= SE.reshape(1,SE.shape[0])

# Question 4
# turn off the axis and gril lines to remove the blue lines in the boder
# check the diff between images to find the difference between eroded and original
#     img=genfromtxt('f3.txt', delimiter=',').astype(int)
#     SE = genfromtxt('SE4.txt', delimiter=',').astype(int)

# Question 5
# check the diff between images to find the difference between eroded and original
#     img=genfromtxt('f3.txt', delimiter=',').astype(int)
#     SE = genfromtxt('SE5.txt', delimiter=',').astype(int)

# Question 6
# check the diff between images to find the difference between eroded and original
#     img=genfromtxt('f3.txt', delimiter=',').astype(int)
#     SE = genfromtxt('SE6.txt', delimiter=',').astype(int)

    vmax = np.max(img)
    vmin = np.min(img)

    operation = 'e'

    padding_value = None
    operation_dilation = None
    operation_erosion = None

    if(operation == 'd'):
        padding_value = vmin
        operation_dilation = True
    elif(operation == 'e'):
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

    print("img: \n", img, end=' \n\n')
    print("img_boundary: \n", img_with_boundary, end=' \n\n')
    print("img_eroded: \n", img_output, end=' \n\n')

    # plot main images
    plt.subplot(1, 4, 1)
    # grid for the image
    ax = plt.gca()
    ax.set_xticks(np.arange(-.5, 10, 1), minor=True)
    ax.set_yticks(np.arange(-.5, 10, 1), minor=True)
    ax.grid(which='minor', color='r', linestyle='-', linewidth=2)
    plt.imshow(SE, cmap='gray', vmin=0, vmax=1)
    plt.title('SE')
    plt.axis('off') if turn_off_axes else None

    # plot main images
    plt.subplot(1, 4, 2)
    # grid for the image
    ax = plt.gca()
    ax.set_xticks(np.arange(-.5, 10, 1), minor=True)
    ax.set_yticks(np.arange(-.5, 10, 1), minor=True)
    ax.grid(which='minor', color='b', linestyle='-', linewidth=1)

    plt.imshow(img, cmap='gray', vmin=0, vmax=vmax)
    plt.title('img')
    plt.axis('off') if turn_off_axes else None

    # Plot the bordered image
    plt.subplot(1, 4, 3)
    # grid for the image
    ax = plt.gca()
    ax.set_xticks(np.arange(-.5, 10, 1), minor=True)
    ax.set_yticks(np.arange(-.5, 10, 1), minor=True)
    ax.grid(which='minor', color='b', linestyle='-', linewidth=1)

    plt.imshow(img_with_boundary, cmap='gray', vmin=0, vmax=vmax)
    plt.title('img_with_boundary')
    plt.axis('off') if turn_off_axes else None

    # Plot the exepected output
    plt.subplot(1, 4, 4)
    ax = plt.gca()
    ax.set_xticks(np.arange(-.5, 10, 1), minor=True)
    ax.set_yticks(np.arange(-.5, 10, 1), minor=True)
    ax.grid(which='minor', color='b', linestyle='-', linewidth=1)

    plt.imshow(img_output, cmap='gray', vmin=0, vmax=vmax)
    plt.title('eroded')
    plt.axis('off') if turn_off_axes else None
    plt.show()


# if __name__ == "__main__":
erosion()
