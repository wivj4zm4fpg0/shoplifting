import argparse
import os

import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('--csv_path', default=None, type=str)
parser.add_argument('--input_dirs', default=None, nargs='*')
parser.add_argument('--width', type=int, default=300)
parser.add_argument('--height', type=int, default=300)
args = parser.parse_args()

csv = pd.read_csv(args.csv_path, sep=' ')

for i in range(len(csv)):
    for input_dir in args.input_dirs:
        class_name = ''
        if csv['class'][i] == 1:
            class_name = 'action'
        elif csv['class'][i] == 0:
            class_name = 'no_action'
        input_dir_path = os.path.join(input_dir, class_name, csv['video_name'][i])
        for image in os.listdir(input_dir_path):
            if '.jpg' not in image:
                continue

            image_path = os.path.join(input_dir_path, image)
            command = 'convert {} -crop {}x{}+{}+{} -resize {}x{} -background "rgb(0, 0, 0)" -gravity center -extent {}x{} {}'.format(
                image_path,
                csv['width'][i],
                csv['height'][i],
                csv['x'][i],
                csv['y'][i],
                args.width,
                args.height,
                args.width,
                args.height,
                image_path
            )
            print(command)
            # os.system(command)
