import argparse
import os
import re

import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument(
    '-if', '--input_csv', default='csv_files/out.csv', type=str
)
parser.add_argument(
    '-id', '--input_directory', default='crop_videos', type=str
)
parser.add_argument(
    '-o', '--output_directory', default='final_crop_videos', type=str
)
parser.add_argument(
    '-w', '--width', default=300, type=int
)
parser.add_argument(
    '-he', '--height', default=300, type=int
)
parser.add_argument(
    '-pn', '--parallel_number', default=-1, type=int,
    help='parallel process number'
)
args = parser.parse_args()

csv = pd.read_csv(args.input_csv, sep=' ')

os.makedirs(args.output_directory, exist_ok=True)


def process(index):
    scale_x = -1
    scale_y = -1
    if csv['width'][index] / csv['height'][index] >= args.width / args.height:
        scale_x = args.width
    else:
        scale_y = args.height
    out_name = '{}_{}.mp4'.format(re.sub(r'\.mp4', '', csv['video_name'][index]),
                                  csv['id'][index])
    command = 'ffmpeg -y -i {} -vf crop={}:{}:{}:{},scale={}:{},pad=width={}:height={}:x={}:y={}:color=black -ss {} -to {} {}'.format(
        os.path.join(args.input_directory, csv['video_name'][index]),
        csv['width'][index], csv['height'][index],
        csv['x'][index], csv['y'][index],
        scale_x, scale_y,
        args.width, args.height,
        int(args.width / 2), int(args.height / 2),
        csv['start_time'][index], csv['end_time'][index],
        os.path.join(args.output_directory, out_name)
    )
    os.system(command)


for i in range(len(csv)):
    process(i)
