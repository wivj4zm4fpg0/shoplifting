import argparse
import os
import re

import pandas as pd
from joblib import Parallel, delayed

parser = argparse.ArgumentParser()
parser.add_argument(
    '-if', '--input_file', default='csv_files/out.csv', type=str
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

csv = pd.read_csv(args.input_file, sep=' ')

os.makedirs(args.output_directory, exist_ok=True)


# for i in range(len(csv['id'])):
#     scale_x = -1
#     scale_y = -1
#     if csv['width'][i] / csv['height'][i] >= args.width / args.height:
#         scale_x = args.width
#     else:
#         scale_y = args.height
#     out_name = '{}_{}.mp4'.format(re.sub(r'\.mp4', '', csv['video_name'][i]), csv['id'][i])
#     os.system(
#         'ffmpeg -y -i {} -vf crop={}:{}:{}:{},scale={}:{},pad=width={}:height={}:x=iw/2:y=ih/2:color=black -ss {} -to {} {}'.format(
#             os.path.join(args.input_directory, csv['video_name'][i]),
#             csv['width'][i], csv['height'][i],
#             csv['x'][i], csv['y'][i],
#             scale_x, scale_y,
#             args.width, args.height,
#             csv['start_time'][i], csv['end_time'][i],
#             os.path.join(args.output_directory, out_name)
#         )
#     )


def process(index):
    scale_x = -1
    scale_y = -1
    if csv['width'][index] / csv['height'][index] >= args.width / args.height:
        scale_x = args.width
    else:
        scale_y = args.height
    out_name = '{}_{}.mp4'.format(re.sub(r'\.mp4', '', csv['video_name'][index]), csv['id'][index])
    os.system(
        'ffmpeg -y -i {} -vf crop={}:{}:{}:{},scale={}:{},pad=width={}:height={}:x=iw/2:y=ih/2:color=black -ss {} -to {} {}'.format(
            os.path.join(args.input_directory, csv['video_name'][index]),
            csv['width'][index], csv['height'][index],
            csv['x'][index], csv['y'][index],
            scale_x, scale_y,
            args.width, args.height,
            csv['start_time'][index], csv['end_time'][index],
            os.path.join(args.output_directory, out_name)
        )
    )


Parallel(n_jobs=args.parallel_number)([delayed(process)(
    index) for index in range(len(csv))
])
