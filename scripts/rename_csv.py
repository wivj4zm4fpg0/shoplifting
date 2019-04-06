# csvファイルのvideo_nameを修正して名前の最後にidと.mp4を付加するスクリプト


import argparse
import re

import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument(
    '--input_file', default='out.csv', type=str
)
parser.add_argument(
    '--output_file', default='out_renamed.csv', type=str
)
args = parser.parse_args()

csv = pd.read_csv(args.input_file, sep=r'\s', engine='python')

with open(args.output_file, 'w') as f:
    f.write('id video_name class start_time end_time x y width height fps\n')
    for i in range(len(csv)):
        out_name = '{}_{}.mp4'.format(re.sub(r'\.mp4', '', csv['video_name'][i]),
                                      csv['id'][i])
        f.write('{} {} {} {} {} {} {} {} {} {}\n'.format(i, out_name, csv['class'][i],
                                                         csv['start_time'][i],
                                                         csv['end_time'][i],
                                                         csv['x'][i], csv['y'][i],
                                                         csv['width'][i],
                                                         csv['height'][i],
                                                         csv['fps'][i]))
