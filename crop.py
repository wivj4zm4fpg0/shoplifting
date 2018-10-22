import re

import pandas as pd

csv = pd.read_csv('out.csv', sep=' ')

with open('final_crop.sh', 'w') as f:
    f.write('#!/bin/bash -eu\n\ncd $1\n\n')
    for i in range(len(csv['id'])):
        out_name = '{}_{}.mp4'.format(re.sub(r'\.mp4', '', csv['video_name'][i]), csv['id'][i])
        f.write('ffmpeg -y -i -ss {} -to {} {}'.format(csv['start_time'], csv['end_time'], out_name))
