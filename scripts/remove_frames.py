import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument(
    '-i', '--input_dir', default=None, type=str
)
parser.add_argument(
    '-n', '--frame_number', default=64, type=int
)
args = parser.parse_args()

for classes in os.listdir(args.input_dir):
    for images in os.listdir(os.path.join(args.input_dir, classes)):
        path = os.path.join(args.input_dir, classes, images)
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
            string = 'rm {}'.format(os.path.join(path, 'image_{:05}.jpg'.format(j)))
            print(string)
            os.system(string)
