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
validation_number = int(len(csv) / divide_rate / 2)

for i in range(divide_rate):
    with open('{}_{}.csv'.format(args.output_file, i + 1), 'w') as f:
        f.write('id video_name class subset\n')
        validation_index_min = validation_number * i
        validation_index_max = validation_number * (i + 1)
        action_count = 0
        no_action_count = 0
        subset = ''
        for j in range(len(csv)):
            if csv['class'][j] == 0:
                no_action_count += 1
                if validation_index_max >= no_action_count > validation_index_min:
                    subset = 'validation'
                else:
                    subset = 'training'
            else:
                action_count += 1
                if validation_index_max >= action_count > validation_index_min:
                    subset = 'validation'
                else:
                    subset = 'training'
            f.write('{} {} {} {}\n'.format(
                csv['id'][j],
                re.sub(r'\.mp4', '', csv['video_name'][j]),
                csv['class'][j],
                subset
            ))
