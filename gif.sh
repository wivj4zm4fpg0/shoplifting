#!/usr/bin/zsh -eu

OUT_NAME=$(echo $1 | sed -e 's:^.*/::g' | sed -e 's/\..*$//g')

ffmpeg -i $1 gifs/$OUT_NAME${2:-}.gif
