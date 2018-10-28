import re
import os

import pandas as pd

csv = pd.read_csv('out.csv', sep=' ')

width = 300
height = 300

with open('final_crop.sh', 'w') as f:
    f.write('#!/bin/bash -eu\n\n')
    for i in range(len(csv['id'])):
        scale_x = -1
        scale_y = -1
        if csv['width'][i] / csv['height'][i] >= 1:
            scale_x = width
        else:
            scale_y = height
        out_name = '{}_{}.mp4'.format(re.sub(r'\.mp4', '', csv['video_name'][i]), csv['id'][i])
        f.write(
            'ffmpeg -y -i {} -vf crop={}:{}:{}:{} -ss {} -to {} {}\n'.format(
                os.path.join('$1', csv['video_name'][i]), csv['width'][i], csv['height'][i], csv['x'][i], csv['y'][i], csv['start_time'][i], csv['end_time'][i],
                os.path.join('$2', out_name)))
