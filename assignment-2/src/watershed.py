import argparse

def main():
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
    
    return 0

if __name__ == "__main__":
    main()
