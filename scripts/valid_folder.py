import argparse
import os
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument(
    '--input_dir', default=None, type=str
)
parser.add_argument(
    '--input_csv', default=None, type=str
)
parser.add_argument(
    '--class_value', default=1, type=int
)
args = parser.parse_args()

csv = pd.read_csv(args.input_csv, sep=' ')
name_list = []
for i in range(len(csv)):
    if csv['class'][i] == args.class_value:
        name_list.append(csv['video_name'][i])

for name in os.listdir(args.input_dir):
    if name not in name_list:
        print(name)
