import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    '-i', '--input_file', default='final_crop_videos', type=str
)
args = parser.parse_args()

for video_name in os.listdir(args.output_file):
    resolution = os.popen(
        'ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0 {}'.format(
            os.path.join(args.output_file, video_name)
        )
    ).read().split('x')
    print('{} = {}x{}'.format(video_name, resolution[0], resolution[1]))
