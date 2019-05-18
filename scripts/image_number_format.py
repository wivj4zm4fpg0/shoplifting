# remove_frames.pyを実行したあと飛び飛びになったフレーム番号を連番になるようにするスクリプト
# さらにframe_numberに達していないフレーム群をその数に達するようにする。
# 例：A|B|C 3ｰ>7にする
# A, A, A | B, B | C, C

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

short_list = [] # frame_numberに達していないフレーム群をここに格納する

# フレーム番号を振り直す
for input_dir in args.input_dirs:
    for classes in os.listdir(input_dir):
        classes_path = os.path.join(input_dir, classes)
        for images in os.listdir(classes_path):
            images_path = os.path.join(classes_path, images)
            image_list = []
            for image in os.listdir(images_path):
                if ".jpg" in image:
                    image_list.append(image)
            image_list = natsorted(image_list) # listdirだと名前順にならないのでこの文で並び替える
            image_length = len(image_list)
            if image_length < args.frame_number:
                short_list.append(images_path)
            for i in range(image_length):
                name = f'image_{i + 1:05}.jpg'
                if image_list[i] == name:
                    continue
                os.rename(
                    os.path.join(images_path, image_list[i]),
                    os.path.join(images_path, name)
                )

# frame_numberに達していないフレーム群を達するようにする
# _image_○○○○○を一時的に作る
for short_images_path in short_list:
    image_list = os.listdir(short_images_path)
    image_list = natsorted(image_list)
    image_length = len(image_list)
    quotient, mod = divmod(args.frame_number, image_length)  # 商とあまり
    j = 0
    k = 0
    for i in range(image_length):
        for _ in range(quotient):
            command = 'cp {} {}'.format(
                os.path.join(short_images_path, image_list[i]),
                os.path.join(short_images_path, f'_image_{j + 1:05}.jpg')
            )
            os.system(command)
            j += 1
        if k != mod:
            command = 'cp {} {}'.format(
                os.path.join(short_images_path, image_list[i]),
                os.path.join(short_images_path, f'_image_{j + 1:05}.jpg')
            )
            os.system(command)
            j += 1
            k += 1

# 今あるimage_○○○○○を全部消して_image_○○○○○をリネームする
for short_images_path in short_list:
    os.system('rm {}'.format(os.path.join(short_images_path, 'image*')))
    image_list = os.listdir(short_images_path)
    image_list = natsorted(image_list)
    for i in range(len(image_list)):
        os.rename(
            os.path.join(short_images_path, image_list[i]),
            os.path.join(short_images_path, f'image_{i + 1:05}.jpg')
        )