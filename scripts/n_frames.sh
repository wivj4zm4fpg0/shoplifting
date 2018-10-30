#!/bin/bash -eu

readonly INPUT_DIR=$1
count=0

for _video_name in $(ls ${INPUT_DIR}); do
    _frame_number=$(ls -1U ${INPUT_DIR}/${_video_name} | wc -l)
    echo ${_frame_number} > ${INPUT_DIR}/${_video_name}/n_frames
    echo ${count} ${_video_name}
    count=$(( count + 1 ))
done
