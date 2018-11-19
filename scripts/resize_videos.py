import argparse
import os
import shutil

parser = argparse.ArgumentParser()
parser.add_argument(
    '-i', '--input_directory', default=None, type=str
)
parser.add_argument(
    '-o', '--output_directory', default=None, type=str
)
parser.add_argument(
    '-w', '--width', default=640, type=int
)
parser.add_argument(
    '-he', '--height', default=480, type=int
)
args = parser.parse_args()

os.makedirs(args.output_directory, exist_ok=True)
for video in os.listdir(args.input_directory):
    scale_x = -1
    scale_y = -1
    input_video_path = os.path.join(args.input_directory, video)
    output_video_path = os.path.join(args.output_directory, video)
    resolution = os.popen(
        'ffprobe -v error -select_streams v:0 -show_entries'
        ' stream=width,height -of csv=s=x:p=0 {}'.format(
            input_video_path
        )
    ).read().split('x')
    if int(resolution[0]) == args.width and int(resolution[1]) == args.height:
        shutil.copy(input_video_path, output_video_path)
        continue
    if int(resolution[0]) / int(resolution[1]) >= args.width / args.height:
        scale_x = args.width
    else:
        scale_y = args.height
    command = 'ffmpeg -y -i {} -vf \
    scale={}:{},pad=width={}:height={}:x=-1:y=-1:color=black {}'.format(
        input_video_path, scale_x, scale_y, args.width, args.height, output_video_path
    )
    os.system(command)
