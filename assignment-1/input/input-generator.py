import numpy as np
import os.path
from skimage import io
from PIL import Image
import csv


def write_SEs():
    SE = np.array([[1, 1, 1, ],
                   [1, 1, 1, ],
                   [1, 1, 1, ]])

    np.savetxt('SE1.txt', SE, delimiter=', ', newline='\n', fmt='%d')

    vertical_SE = np.array([[1], [1], [1]])
    np.savetxt('SE2.txt', vertical_SE, delimiter=', ', newline='\n', fmt='%d')

    horizontal_SE = np.array([[1, 1, 1]])
    np.savetxt('SE3.txt', horizontal_SE,
               delimiter=', ', newline='\n', fmt='%d')

    square_five_ones_SE = np.ones((5, 5), int)
    np.savetxt('SE4.txt', square_five_ones_SE,
               delimiter=', ', newline='\n', fmt='%d')

    # backward diagonal
    backward_nine_SE = np.eye(9)
    np.savetxt('SE5.txt', backward_nine_SE,
               delimiter=', ', newline='\n', fmt='%d')

    # forward diagonal
    np.savetxt('SE6.txt', np.flip(backward_nine_SE, 0),
               delimiter=', ', newline='\n', fmt='%d')

    # asymmetric SE not containing the center
    SE = np.array([
        [1, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 1, 0, 1],
        [0, 0, 1, 0],
        [1, 0, 0, 0]
    ])
    np.savetxt('SE_asym_no_origin.txt', SE,
               delimiter=', ', newline='\n', fmt='%d')

    # for wolf image
    SE = np.array([[0, 1, 0],
                   [1, 1, 1],
                   [0, 1, 0]])
    np.savetxt('SE7.txt', SE,
               delimiter=', ', newline='\n', fmt='%d')


def input_img_to_csv(filename):
    img = io.imread(filename, as_gray=True)
    img = img/np.max(img)*255
    img = img.astype(np.uint8)
    np.savetxt(os.path.splitext(filename)[0] + ".txt", img,
               delimiter=', ', newline='\n', fmt='%d')


def images_to_csv():
    # These are different inputs that we are converting to csv file format
    input_img_to_csv("covid.png")
    input_img_to_csv("fp.png")
    input_img_to_csv("medusa.jpg")
    input_img_to_csv("roots.png")
    input_img_to_csv("sample_img1.jpg")
    input_img_to_csv("sample_img2.jpg")
    input_img_to_csv("sample_img3.jpg")
    input_img_to_csv("wolf.jpg")

if __name__ == "__main__":
    write_SEs()
    images_to_csv()
