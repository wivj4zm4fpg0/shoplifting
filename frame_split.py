import pandas as pd
import re
import os

csv = pd.read_csv('out.csv', sep=' ')

with open('frame_split.sh', 'w') as f:
    f.write('#!/bin/bash -eu\n\n')
    for i in range(len(csv['id'])):
        out_name = '{}_{}.mp4'.format(re.sub(r'\.mp4', '', csv['video_name'][i]), csv['id'][i])
        out_dir = re.sub(r'\.mp4', '', out_name)
        f.write('mkdir -p {}\n'.format(os.path.join('$2', out_dir)))
        f.write('ffmpeg -y -i {} -r {} {}\n'.format(os.path.join('$1', out_name), csv['fps'][i],
                                                    os.path.join('$2', out_dir, 'image_%05d.jpg')))
