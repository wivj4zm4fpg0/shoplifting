#!/bin/bash -eu

cd $1

for VIDEO in $(ls); do
    if ! echo $VIDEO | grep -q ".mp4"; then
        NAME=$(echo $VIDEO | sed -e 's/\..*$//g').mp4
        ffmpeg -i $VIDEO -y -strict -2 $NAME
    fi
done
