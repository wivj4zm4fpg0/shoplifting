import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument(
    '-i', '--input_dirs', default=None, nargs='*'
)
parser.add_argument(
    '-n', '--frame_number', default=64, type=int
)
args = parser.parse_args()

for input_dir in args.input_dirs:
    for classes in os.listdir(input_dir):
        classes_path = os.path.join(input_dir, classes)
        for images in os.listdir(classes_path):
            path = os.path.join(classes_path, images)
            frames = len(os.listdir(path))
            space = frames / args.frame_number
            ls = list(range(1, frames + 1))
            i = 1
            while i < frames + 1:
                try:
                    ls.remove(int(i))
                except ValueError:
                    pass
                i += space
            for j in ls:
                string = 'rm {}'.format(
                    os.path.join(path, 'image_{:05}.jpg'.format(j)))
                # print(string)
                os.system(string)
