import os.path
import argparse
import numpy as np
from numpy import genfromtxt
from matplotlib import pyplot as plt
plt.rcParams["figure.figsize"] = (25, 5)


def morph_operation(img, SE, operation_type, direction, output_filename):

    if(direction == "vertical"):
        SE = SE.reshape(SE.shape[0], 1)
    elif(direction == "horizontal"):
        SE = SE.reshape(1, SE.shape[0])

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

    ################ Plot Save #########################

    plt.subplot(1, 4, 1)
    # grid for the image
    ax = plt.gca()
    ax.set_xticks(np.arange(-.5, 10, 1), minor=True)
    ax.set_yticks(np.arange(-.5, 10, 1), minor=True)
    ax.grid(which='minor', color='b', linestyle='-', linewidth=1)
    plt.imshow(SE, cmap='gray', vmin=0, vmax=1)
    plt.title('SE')
    # plt.axis('off') if turn_off_axes else None

    # plot main images
    plt.subplot(1, 4, 2)
    # grid for the image
    ax = plt.gca()
    ax.set_xticks(np.arange(-.5, 10, 1), minor=True)
    ax.set_yticks(np.arange(-.5, 10, 1), minor=True)
    ax.grid(which='minor', color='b', linestyle='-', linewidth=1)

    plt.imshow(img, cmap='gray', vmin=0, vmax=vmax)
    plt.title('image')
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
    plt.title('Image after operation')
    plt.axis('off') if turn_off_axes else None
    # plt.show()
    plt.savefig(".\output\\"+ output_filename + ".png", bbox_inches='tight')

    ##################################################

    return img_output


def main():
    # Create a parser
    parser = argparse.ArgumentParser(
        usage="main.py [-h] (-d SE f f_out | -e SE f f_out)",
        formatter_class=argparse.RawTextHelpFormatter
    )
    # Make the argument options mutually exclusive
    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument("-d", type=str, nargs=3,
                       metavar=('SE', 'f', 'f_out'),
                       help="perform dilation\n SE : Structuring element\n f  : Input filename in CSV Format\n f_out: Output filename in CSV Format"
                       )

    group.add_argument("-e", type=str, nargs=3,
                       metavar=('SE', 'f', 'f_out'),
                       help="perform erosion\n SE : Structuring element\n f  : Input filename in CSV Format\n f_out: Output filename in CSV Format"
                       )
    args = parser.parse_args()

    # setting up the filenames received as an argument through command line
    filenames = None
    operation_type = None
    direction = None
    if args.d:
        filenames = args.d
        operation_type = 'd'
    elif args.e:
        filenames = args.e
        operation_type = 'e'

    # read the files and the CSVs
    SE = genfromtxt(filenames[0], delimiter=',').astype(int)
    img = genfromtxt(filenames[1], delimiter=',').astype(int)

    if("SE2.txt" in filenames[0]):
        direction = "vertical"
    if("SE3.txt" in filenames[0]):
        direction = "horizontal"
    
    img_output = morph_operation(img, SE, operation_type, direction, os.path.splitext(filenames[2])[0])

    np.savetxt(".\output\\" + filenames[2], img_output,
               delimiter=', ', newline='\n', fmt='%d')


if __name__ == "__main__":
    main()
