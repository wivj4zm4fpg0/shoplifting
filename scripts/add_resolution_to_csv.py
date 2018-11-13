import argparse
import os

import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument(
    '-i', '--input_csv', default=None, type=str
)
parser.add_argument(
    '-id', '--input_dir', default=None, type=str
)
parser.add_argument(
    '-o', '--output_csv', default=None, type=str
)
args = parser.parse_args()

csv = pd.read_csv(args.input_csv, sep=' ')

with open(args.output_csv, 'w') as f:
    f.write(
        'id video_name class start_time end_time x y width height original_width original_height')
    for i in range(len(csv)):
        resolution = os.popen(
            'ffprobe -v error -select_streams v:0 -show_entries'
            ' stream=width,height -of csv=s=x:p=0 {}'.format(
                os.path.join(args.input_csv, video_name)
            )
        ).read().split('x')
