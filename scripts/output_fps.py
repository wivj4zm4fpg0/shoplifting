import argparse

import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument(
    '--input_file', default='under_sampling.csv', type=str
)
parser.add_argument(
    '--output_file', default='out.csv', type=str
)
parser.add_argument(
    '--frames_number', default=64, type=int
)
args = parser.parse_args()

csv = pd.read_csv(args.input_file, sep=' ')


def format_time(string):
    times = string.split(":")
    during_time = int(times[1]) * 60 + int(times[2])
    return during_time


def get_fps(duration, frames_number):
    fps = 1
    while fps * duration < frames_number:
        fps += 1
    return fps


with open(args.output_file, 'w') as f:
    f.write('id video_name class start_time end_time x y width height fps\n')
    for i in range(len(csv['id'])):
        time = format_time(csv['end_time'][i]) - format_time(csv['start_time'][i])
        f.write('{} {} {} {} {} {} {} {} {} {}\n'.format(i, csv['video_name'][i], csv['class'][i], csv['start_time'][i],
                                                         csv['end_time'][i], csv['x'][i], csv['y'][i], csv['width'][i],
                                                         csv['height'][i], get_fps(time, args.frames_number)))
