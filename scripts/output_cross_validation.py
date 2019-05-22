# 交差検証法のために1つのcsvからsubsetを記述した5つのcsvファイルを生成するスクリプト


import argparse
import re

import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument(
    '-i', '--input_file', default='input.csv', type=str
)
parser.add_argument(
    '-o', '--output_file', default='out', type=str
)
parser.add_argument(
    '--divide_rate', default=5, type=int
)
args = parser.parse_args()

csv = pd.read_csv(args.input_file, sep=r'\s', engine='python')
csv = csv.sort_values(by=['class', 'id'], ascending=True)

divide_rate = args.divide_rate
action_len = len([i for i in csv['class'] if i == 1])
no_action_len = len([i for i in csv['class'] if i == 0])
action_val_len = int(action_len / divide_rate)
no_action_val_len = int(no_action_len / divide_rate)

for i in range(divide_rate):
    with open('{}_{}.csv'.format(args.output_file, i + 1), 'w') as f:
        f.write('id video_name class subset\n')
        action_val_index_min = action_val_len * i
        action_val_index_max = action_val_len * (i + 1)
        no_action_val_index_min = no_action_val_len * i
        no_action_val_index_max = no_action_val_len * (i + 1)
        action_count = 0
        no_action_count = 0
        subset = ''
        for j in range(len(csv)):
            if csv['class'][j] == 0:
                no_action_count += 1
                if no_action_val_index_max >= no_action_count > no_action_val_index_min:
                    subset = 'validation'
                else:
                    subset = 'training'
            else:
                action_count += 1
                if action_val_index_max >= action_count > action_val_index_min:
                    subset = 'validation'
                else:
                    subset = 'training'
            f.write('{} {}_{} {} {}\n'.format(
                csv['id'][j],
                re.sub(r'\.mp4', '', csv['video_name'][j]),
                csv['id'][j],
                csv['class'][j],
                subset
            ))
