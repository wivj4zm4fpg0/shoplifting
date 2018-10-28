import argparse
import os
import shutil

import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument(
    'input_file', default='out.csv', type=str
)
parser.add_argument(
    'input_directory', default=None, type=str
)
args = parser.parse_args()

csv = pd.read_csv(args.input_file, sep=' ')

no_action = os.path.join(args.input_directory, 'no_action')
action = os.path.join(args.input_directory, 'action')

os.makedirs(no_action, exist_ok=True)
os.makedirs(action, exist_ok=True)

for i in range(len(csv)):
    path = os.path.join(args.input_directory, csv['video_name'][i])
    if csv['class'][i] == 0:
        shutil.move(path, no_action)
    else:
        shutil.move(path, action)
