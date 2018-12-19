import os
import argparse
import shutil
from distutils.dir_util import copy_tree

import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('--input_paths', default=None, nargs='*')
parser.add_argument('--csv_path', default=None, type=str)
parser.add_argument('--remove_base_name', action='store_true')
args = parser.parse_args()

csv = pd.read_csv(args.csv_path, sep=' ')

for i in range(len(csv)):
    for input_path in args.input_paths:
        class_name = ''
        if csv['class'][i] == 1:
            class_name = 'action'
        elif csv['class'][i] == 0:
            class_name = 'no_action'
        copy_tree(os.path.join(input_path, class_name, csv['base_name'][i]),
                  os.path.join(input_path, class_name, csv['video_name'][i]))

if args.remove_base_name:
    for i in range(len(csv)):
        for input_path in args.input_paths:
            class_name = ''
            if csv['class'][i] == 1:
                class_name = 'action'
            elif csv['class'][i] == 0:
                class_name = 'no_action'
            base_name_path = os.path.join(input_path, class_name, csv['base_name'][i])
            if os.path.exists(base_name_path):
                shutil.rmtree(base_name_path)
