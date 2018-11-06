import argparse
import os
import re

import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument(
    '--input_file', default='out.csv', type=str
)
parser.add_argument(
    '--output_file', default='frame_split.sh', type=str
)
args = parser.parse_args()

csv = pd.read_csv(args.input_file, sep=' ')

with open(args.output_file, 'w') as f:
    f.write('#!/bin/bash -eu\n\n')
    for i in range(len(csv['id'])):
        out_name = '{}_{}.mp4'.format(re.sub(r'\.mp4', '', csv['video_path'][i]), csv['id'][i])
        out_dir = re.sub(r'\.mp4', '', out_name)
        f.write('mkdir -p {}\n'.format(os.path.join('$2', out_dir)))
        f.write('ffmpeg -y -i {} -r {} {}\n'.format(os.path.join('$1', out_name), csv['fps'][i],
                                                    os.path.join('$2', out_dir, 'image_%05d.jpg')))
