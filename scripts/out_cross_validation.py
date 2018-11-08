import argparse

import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument(
    '-i', '--input_file', default='final_crop_videos', type=str
)
parser.add_argument(
    '-o', '--output_file', default='cross_validation', type=str
)
args = parser.parse_args()

csv = pd.read_csv(args.input_file, sep=' ')
csv = csv.sort_values(by=['class', 'id'], ascending=True)

divide_rate = 5
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
                if validation_index_max > no_action_count >= validation_index_min:
                    subset = 'validation'
                else:
                    subset = 'training'
            else:
                action_count += 1
                if validation_index_max > action_count >= validation_index_min:
                    subset = 'validation'
                else:
                    subset = 'training'
            f.write('{} {} {} {}\n'.format(
                csv['id'][j],
                csv['video_name'][j],
                csv['class'][j],
                subset
            ))
