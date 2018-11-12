import argparse
import os
import shutil
import re

import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument(
    'input_file', default='csv_files/out.csv', type=str
)
parser.add_argument(
    'output_file', default=None, type=str
)
args = parser.parse_args()

csv = pd.read_csv(args.input_file, sep=' ')

no_action = os.path.join(args.output_file, 'no_action')
action = os.path.join(args.output_file, 'action')

suffix = ''
if '.mp4' in os.listdir(args.output_file)[0]:
    suffix = '.mp4'
os.makedirs(no_action, exist_ok=True)
os.makedirs(action, exist_ok=True)

for i in range(len(csv)):
    path = '{}_{}{}'.format(
        re.sub(r'\.mp4', '', os.path.join(args.output_file, csv['video_name'][i])),
        csv['id'][i], suffix
    )
    if csv['class'][i] == 0:
        shutil.move(path, no_action)
    else:
        shutil.move(path, action)
