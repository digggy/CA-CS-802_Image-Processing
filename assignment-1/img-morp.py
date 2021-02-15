# Import argparse library
import argparse


# Create a parser
parser = argparse.ArgumentParser()
# Add the argument
parser.add_argument('-d', type=str, required=True)

# Execute the parse_args() method
args = parser.parse_args()



