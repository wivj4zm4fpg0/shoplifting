#!/usr/bin/zsh -eu

OUT_NAME=$(echo $1 | sed -e 's:^.*/::g' | sed -e 's/\..*$//g')
EXTENSION=$(echo $1 | sed -e 's/^[^.]*//g')

ffmpeg -i $1 -vf scale=$2:$3 scale/$OUT_NAME${4:-}$EXTENSION
