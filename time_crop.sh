#!/bin/zsh -eu

OUT_NAME=$(echo $1 | sed -e 's:^.*/::g' | sed -e 's/\..*$//g')
EXTENSION=$(echo $1 | sed -e 's/^[^.]*//g')

ffmpeg -i $1 -ss $2 -t $3 time_crop/$OUT_NAME${4:-}$EXTENSION
