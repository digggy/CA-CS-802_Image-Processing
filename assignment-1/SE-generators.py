import numpy as np
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
    SE = np.array([[0, 1, 0 ],
                [1, 0, 1 ],
                [0, 0, 1 ]])
    np.savetxt('SE_asym_no_origin.txt', SE ,
            delimiter=', ', newline='\n', fmt='%d')

if __name__ == "__main__":
    write_SEs()
