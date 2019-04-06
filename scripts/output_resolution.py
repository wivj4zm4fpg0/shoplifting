# 動画の解像度を出力するだけのスクリプト


import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    '-i', '--input_dir', default='final_crop_videos', type=str
)
args = parser.parse_args()

for video_name in os.listdir(args.input_dir):
    resolution = os.popen(
        'ffprobe -v error -select_streams v:0 -show_entries'
        ' stream=width,height -of csv=s=x:p=0 {}'.format(
            os.path.join(args.input_dir, video_name)
        )
    ).read().split('x')
    print('{} = {}x{}'.format(video_name, resolution[0], resolution[1]))
