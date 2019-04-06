#!/bin/bash -eu

# フレームに分解済みのフォルダにフレーム数が記述されたn_framesを作成するスクリプト

readonly INPUT_DIR=$1
count=0

for _classes in $(ls ${INPUT_DIR}); do
    for _images in $(ls ${INPUT_DIR}/${_classes}); do
        _frame_number=$(ls -1U ${INPUT_DIR}/${_classes}/${_images} | wc -l)
        echo ${_frame_number} > ${INPUT_DIR}/${_classes}/${_images}/n_frames
        echo ${count} ${_classes}
        count=$(( count + 1 ))
    done
done
