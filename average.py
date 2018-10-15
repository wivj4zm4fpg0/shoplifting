import pandas as pd
import argparse
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument(
    'input_file', default=None, type=str
)
parser.add_argument(
    '--start_number', default=0, type=int
)
parser.add_argument(
    '--end_number', default=None, type=int
)
args = parser.parse_args()

table = pd.read_csv(args.input_file, sep=' ')

width = np.empty(0)
height = np.empty(0)

if not args.end_number:
    args.end_number = len(table['id'])

for i in range(args.start_number, args.end_number):
    width = np.append(width, table['width'][i])
    height = np.append(height, table['height'][i])

print('average width = {}'.format(np.mean(width)))
print('average height = {}'.format(np.mean(height)))
