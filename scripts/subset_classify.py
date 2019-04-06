# ランダムに訓練、テストデータに分割するスクリプト
# divide_rateで分割する割合を調整できる


import argparse
import operator
import random
import re

import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument(
    '-i', '--input_file', default='out.csv', type=str
)
parser.add_argument(
    '-o', '--output_file', default='subset_annotation.csv', type=str
)
parser.add_argument(
    '--divide_rate', default=5, type=int
)
args = parser.parse_args()

csv = pd.read_csv(args.input_file, sep=r'\s', engine='python')
action_index = 0
no_action_index = 0
subset = {}

random_csv = list(range(len(csv)))
random.shuffle(random_csv)

divide_rate = args.divide_rate
threshold = int((len(csv) - len(csv) / divide_rate) / 2)

with open(args.output_file, 'w') as f:
    f.write('id video_name class subset\n')
    for i in random_csv:
        if csv['class'][i] == 0:
            if no_action_index <= threshold:
                subset[i] = 'training'
            else:
                subset[i] = 'validation'
            no_action_index += 1
        else:
            if action_index <= threshold:
                subset[i] = 'training'
            else:
                subset[i] = 'validation'
            action_index += 1

    sorted_subset = sorted(subset.items(), key=operator.itemgetter(0))
    for i in range(len(csv)):
        f.write('{} {} {} {}\n'.format(
            csv['id'][i],
            '{}_{}'.format(re.sub(r'\.mp4', '', csv['video_name'][i]), csv['id'][i]),
            csv['class'][i],
            sorted_subset[i][1]
        ))
