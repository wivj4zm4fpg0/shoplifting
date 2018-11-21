import argparse
import os
import re

parser = argparse.ArgumentParser()
parser.add_argument(
    '-i', '--input_dir', default=None, type=str
)
args = parser.parse_args()

for file in os.listdir(args.input_dir):
    os.rename(
        os.path.join(args.input_dir, file),
        os.path.join(args.input_dir, 'video-' + file)
    )

for file in os.listdir(args.input_dir):
    if '.mp4' not in file:
        output_name = re.sub(r'\..*$', '.mp4', file)
        print('ffmpeg -y -i {} {}'.format(
            os.path.join(args.input_dir, file),
            os.path.join(args.input_dir, output_name)
        ))
