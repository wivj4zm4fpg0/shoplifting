import argparse
import os
import re

import numpy as np
import pandas as pd


# 00:01:10 -> 70 に変換
def format_time(string: str) -> int:
    times = string.split(":")
    during_time = int(times[1]) * 60 + int(times[2])
    return during_time


# 70 -> 00:01:10 に変換
def time_format(time: int) -> str:
    minute, second = divmod(time, 60)
    return f'00:{minute:02}:{second:02}'


parser = argparse.ArgumentParser()
parser.add_argument(
    '--input_directory', default=None, type=str
)
parser.add_argument(
    '--output_directory', default=None, type=str
)
parser.add_argument(
    '--input_csv', default=None, type=str
)
parser.add_argument(
    '--split_time', default=5, type=int
)
parser.add_argument(
    '--write_file_path', default=None, type=str
)
parser.add_argument(
    '--during_time', default=10, type=int
)
args = parser.parse_args()

os.makedirs(args.output_directory, exist_ok=True)

csv = pd.read_csv(args.input_csv, sep=' ')

if args.write_file_path:
    with open(args.write_file_path, 'w') as f:
        f.write('#!/bin/bash -eu\n')

j = 0
for i in range(len(csv)):
    end_time = format_time(csv['end_time'][i])
    current_start_time = format_time(csv['start_time'][i])
    current_end_time = current_start_time + args.during_time
    while current_end_time <= end_time:
        if not np.isnan(csv['suffix'][i]):
            out_name = '{}_{}_{}.mp4'.format(
                j,
                re.sub(r'\.mp4', '', csv['video_name'][i]),
                int(csv['suffix'][i])
            )
        else:
            out_name = '{}_{}.mp4'.format(
                j,
                re.sub(r'\.mp4', '', csv['video_name'][i])
            )
        input_path = os.path.join(args.input_directory, csv['video_name'][i])
        command = 'ffmpeg -y -i {} -ss {} -to {} {}'.format(
            input_path,
            time_format(current_start_time),
            time_format(current_end_time),
            os.path.join(args.output_directory, out_name)
        )
        # print(command)
        os.system(command)
        if not os.path.isfile(input_path):
            print(input_path)
        if args.write_file_path:
            with open(args.write_file_path, 'a') as f:
                f.write(f'{command}\n')

        j += 1

        if current_end_time == end_time:
            break

        current_start_time += args.split_time

        if current_end_time + args.split_time > end_time:
            current_end_time = end_time
        else:
            current_end_time += args.split_time
