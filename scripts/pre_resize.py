import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    '-i', '--input_file', default='final_crop_videos', type=str
)
args = parser.parse_args()

for video_name in os.listdir(args.input_file):
    name = os.path.join(args.input_file, video_name)
    resolution = os.popen(
        'ffprobe -v error -select_streams v:0 -show_entries'
        ' stream=width,height -of csv=s=x:p=0 {}'.format(
            name
        )
    ).read().split('x')
    if int(resolution[0]) >= 1000 or int(resolution[1]) >= 1000:
        os.system(
            'ffmpeg -y -i {} -vf scale=iw/2:ih/2 {}'.format(
                name,
                name
            )
        )
