import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument(
    '-i', '--input_dir', default=None, type=str
)
parser.add_argument(
    '-fn', '--frame_number', default=64, type=int
)
args = parser.parse_args()

for classes in os.listdir(args.input_dir):
    classes_path = os.path.join(args.input_dir, classes)
    for images in os.listdir(classes_path):
        images_path = os.path.join(classes_path, images)
        image_list = []
        listdir = os.listdir(images_path)
        for image in listdir:
            if ".jpg" in image:
                image_list.append(image)
        for i in range(len(image_list)):
            name = 'image_{:05}.jpg'.format(i + 1)
            os.rename(os.path.join(images_path, image_list[i]),
                      os.path.join(images_path, name))
        i = len(listdir) + 1
        if args.frame_number > i:
            j = 0
            while i <= args.frame_number:
                os.system('cp {} {}'.format(
                    os.path.join(images_path, image_list[j]),
                    os.path.join(images_path, 'image_{:05}.jpg'.format(i))
                ))
                i += 1
                j += 1
                if j == len(listdir):
                    j = 0
