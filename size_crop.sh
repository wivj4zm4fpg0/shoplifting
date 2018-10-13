#!/usr/bin/zsh -eu

OUT_NAME=$(echo $1 | sed -e 's:^.*/::g' | sed -e 's/\..*$//g')
EXTENSION=$(echo $1 | sed -e 's/^[^.]*//g')

ffmpeg -i $1 -vf crop=320:240:$2:$3 size_crop/$OUT_NAME${4:-}$EXTENSION
