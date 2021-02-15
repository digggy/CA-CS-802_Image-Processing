import argparse
from numpy import genfromtxt

def main():
    # Create a parser
    parser = argparse.ArgumentParser(
        usage="main.py [-h] (-d SE f f_out | -e SE f f_out)",
        formatter_class=argparse.RawTextHelpFormatter
    )
    # Make the argument options mutually exclusive
    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument("-d", type=str, nargs=3,
        metavar=('SE','f','f_out'),
        help="perform dilation\n SE : Structuring element\n f  : Input filename in CSV Format\n f_out: Output filename in CSV Format"
    )
        
    group.add_argument("-e", type=str, nargs=3,
        metavar=('SE','f','f_out'),
        help="perform erosion\n SE : Structuring element\n f  : Input filename in CSV Format\n f_out: Output filename in CSV Format"
    )
    args = parser.parse_args()

    # setting up the filenames received as an argument through command line 
    filenames=None
    if args.d:
        filenames = args.d 
    elif args.e:
        filenames = args.e

    print(filenames)

    # read the files and the CSVs
    se = genfromtxt(filenames[0], delimiter=',').astype(int)
    f = genfromtxt(filenames[1], delimiter=',').astype(int)

    print(se)
    print(f)


if __name__ == "__main__":
    main()