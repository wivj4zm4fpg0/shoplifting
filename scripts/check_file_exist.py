import argparse
import os

import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('--input_paths', default=None, nargs='*')
parser.add_argument('--csv_path', default=None, type=str)
args = parser.parse_args()

csv = pd.read_csv(args.csv_path, sep=' ')

for i in range(len(csv)):
    for input_path in args.input_paths:

        class_index = csv['class'][i]
        assert class_index in [0, 1]

        class_name = ''
        if class_index == 1:
            class_name = 'action'
        elif class_index == 0:
            class_name = 'no_action'

        path = os.path.join(input_path, class_name, csv['base_name'][i])
        if os.path.exists(path):
            pass
            # print(f'exist {path}')
        else:
            print(f'not exist {path}')
