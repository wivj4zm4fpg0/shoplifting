#!/bin/zsh -eu

FILE_NAME=$(echo $1 | sed -e 's/\.[^\.]*$//g' | sed -e 's:^.*/::g')
TYPE=farn
IMAGE_PATH=images/$FILE_NAME
FLOW_X_PATH=flow/$TYPE/flow_x/$FILE_NAME
FLOW_Y_PATH=flow/$TYPE/flow_y/$FILE_NAME

mkdir -p $IMAGE_PATH $FLOW_X_PATH $FLOW_Y_PATH

extract_gpu -f=$1 -x=$FLOW_X_PATH/image -y=$FLOW_Y_PATH/image -i=$IMAGE_PATH/image -t=0 -o=dir -s=10 -n=0
