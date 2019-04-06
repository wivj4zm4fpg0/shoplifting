# csvファイルをもとに動画群を時間で切り取りを行うスクリプト


import argparse
import os
import re

import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument(
    '--input_csv', default='csv_files/out.csv', type=str
)
parser.add_argument(
    '--input_directory', default='crop_videos', type=str
)
parser.add_argument(
    '--output_directory', default='final_crop_videos', type=str
)
parser.add_argument(
    '-pn', '--parallel_number', default=-1, type=int,
    help='parallel process number'
)
args = parser.parse_args()

csv = pd.read_csv(args.input_csv, sep=r'\s', engine='python')

os.makedirs(args.output_directory, exist_ok=True)


def process(index):
    out_name = '{}_{}.mp4'.format(re.sub(r'\.mp4', '', csv['video_name'][index]),
                                  csv['id'][index])
    command = 'ffmpeg -y -i {} -ss {} -to {} {}'.format(
        os.path.join(args.input_directory, csv['video_name'][index]),
        csv['start_time'][index],
        csv['end_time'][index], os.path.join(args.output_directory, out_name)
    )
    os.system(command)


for i in range(len(csv)):
    process(i)
