import argparse
import os.path
import numpy as np
from numpy import genfromtxt

import matplotlib.pyplot as plt
from skimage import color, io, data
from skimage.color import rgb2gray
plt.rcParams["figure.figsize"] = (20,20)

def display(img):
    # Show image
    plt.figure(figsize = (5,5))
    plt.imshow(img)
    plt.axis('off')
    plt.show()

def main():
    # Create a parser
    my_parser = argparse.ArgumentParser(description='Perform watershed')
    
    my_parser.add_argument(
        '-i',
        '--input',
        dest="input",
        metavar='PATH',
        type=str,
        help='the path to input file')
    
    my_parser.add_argument(
        '-n'
        '--neighbours',
        dest="neighbours",
        metavar='N',
        type=int,
        help='number of neighbours')
    
    my_parser.add_argument(
        '-o'
        '--output',
        dest='output',
        metavar='PATH',
        type=str,
        help='the path to outputfile')
    
    args = my_parser.parse_args()
    
    inputfile = args.input
    if inputfile and os.path.isfile(inputfile):
        input_image_extension = os.path.splitext(inputfile)[1]
        img = None
        if(input_image_extension == ".png" or input_image_extension == ".jpg" or input_image_extension == ".jgeg"):
            img = io.imread(inputfile, as_gray=True)
            img = img/np.max(img)*255
            img = img.astype(np.uint8)
        elif (input_image_extension == ".txt"):
            img = genfromtxt(inputfile, delimiter=',').astype(int)
            img -= np.min(img)
            img = img/np.max(img)
    # display(img)
    
    return 0

if __name__ == "__main__":
    main()
