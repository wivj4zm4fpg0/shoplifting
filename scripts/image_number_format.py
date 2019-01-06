import argparse
import os

from natsort import natsorted

parser = argparse.ArgumentParser()
parser.add_argument(
    '--input_dirs', default=None, nargs='*'
)
parser.add_argument(
    '--frame_number', default=64, type=int
)
args = parser.parse_args()

for input_dir in args.input_dirs:
    for classes in os.listdir(input_dir):
        classes_path = os.path.join(input_dir, classes)
        for images in os.listdir(classes_path):
            images_path = os.path.join(classes_path, images)
            image_list = []
            for image in os.listdir(images_path):
                if ".jpg" in image:
                    image_list.append(image)
            image_list = natsorted(image_list)
            image_length = len(image_list)
            for i in range(image_length):
                name = f'image_{i + 1:05}.jpg'
                if image_list[i] == name:
                    continue
                os.rename(
                    os.path.join(images_path, image_list[i]),
                    os.path.join(images_path, name)
                )
            if args.frame_number > image_length:
                i = image_length + 1
                j = 0
                while i <= args.frame_number:
                    command = 'cp {} {}'.format(
                        os.path.join(images_path, image_list[j]),
                        os.path.join(images_path, f'image_{i:05}.jpg')
                    )
                    # print(command)
                    os.system(command)
                    i += 1
                    j += 1
                    if j == image_length:
                        j = 0
