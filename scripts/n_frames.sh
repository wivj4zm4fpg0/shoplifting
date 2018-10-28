#!/bin/bash -eu

readonly INPUT_DIR=$1
count=0

for _video_name in $(ls ${INPUT_DIR}); do
    _frame_number=$(ls -1 ${INPUT_DIR}/${_video_name} | wc -l)
    echo ${_frame_number} > n_frames
    echo ${count} ${_video_name}
    count=$(( count + 1 ))
done
