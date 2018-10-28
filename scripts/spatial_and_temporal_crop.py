import argparse
import os
import re

import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument(
    '--input_file', default='out.csv', type=str
)
parser.add_argument(
    '--output_file', default='final_crop.sh', type=str
)
parser.add_argument(
    '--width', default=300, type=int
)
parser.add_argument(
    '--height', default=300, type=int
)
args = parser.parse_args()

csv = pd.read_csv(args.input_file, sep=' ')

with open(args.output_file, 'w') as f:
    f.write('#!/bin/bash -eu\n\n')
    for i in range(len(csv['id'])):
        scale_x = -1
        scale_y = -1
        if csv['width'][i] / csv['height'][i] >= 1:
            scale_x = args.width
        else:
            scale_y = args.height
        out_name = '{}_{}.mp4'.format(re.sub(r'\.mp4', '', csv['video_name'][i]), csv['id'][i])
        f.write(
            'ffmpeg -y -i {} -vf crop={}:{}:{}:{},scale={}:{},pad=width={}:height={}:x=iw/2:y=ih/2:color=black -ss {} -to {} {}\n'.format(
                os.path.join('$1', csv['video_name'][i]), csv['width'][i], csv['height'][i], csv['x'][i], csv['y'][i],
                scale_x, scale_y, args.width, args.height, csv['start_time'][i], csv['end_time'][i],
                os.path.join('$2', out_name)))
