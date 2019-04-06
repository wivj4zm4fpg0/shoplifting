# クラスファイルを作りそこに動画を移動させるスクリプト


import argparse
import os
import shutil
import re

import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument(
    'input_file', default='csv_files/out.csv', type=str
)
parser.add_argument(
    'output_file', default=None, type=str
)
parser.add_argument(
    '--add_id_to_video', action='store_true',
    help='動画の末尾にidを追加して移動させる'
)
parser.set_defaults(add_id_to_video=False)
args = parser.parse_args()

csv = pd.read_csv(args.input_file, sep=r'\s', engine='python')

no_action = os.path.join(args.output_file, 'no_action')
action = os.path.join(args.output_file, 'action')

os.makedirs(no_action, exist_ok=True)
os.makedirs(action, exist_ok=True)

# 元のフォルダーにmp4ファイルがあるならsuffixにmp4を追加する
suffix = ''
if '.mp4' in os.listdir(args.output_file)[0]:
    suffix = '.mp4'

for i in range(len(csv)):
    output_file_path = os.path.join(
        args.output_file,
        csv['video_name'][i]
    )
    if args.add_id_to_video:
        path = '{}_{}{}'.format(
            re.sub(r'\.mp4', '', output_file_path),
            csv['id'][i],
            suffix
        )
    else:
        path = output_file_path
    if csv['class'][i] == 0:
        shutil.move(path, no_action)
    else:
        shutil.move(path, action)
