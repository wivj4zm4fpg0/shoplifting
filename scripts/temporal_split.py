import argparse
import os

import pandas as pd


def format_time(string: str) -> int:
    times = string.split(":")
    during_time = int(times[1]) * 60 + int(times[2])
    return during_time


def time_format(time: int) -> str:
    minute = time / 60
    second = time // 60
    return '00:{:02}:{:02}'.format(minute, second)


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
    '--split_time', default=10, type=int
)
args = parser.parse_args()

os.makedirs(args.output_directory, exist_ok=True)

csv = pd.read_csv(args.input_csv)

for i in range(len(csv)):
    end_time = format_time(csv['end_time'][i])
    current_start_time = format_time(csv['start_time'][i])
    current_end_time = current_start_time + args.split_time
    while current_end_time < end_time:
        os.system('ffmpeg -y -i {} -ss {} -to {} {}'.format(

        ))
        current_start_time += args.split_time
        current_end_time += args.split_time
