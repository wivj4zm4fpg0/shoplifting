#!/bin/bash -eu

cd $1
for _name in $(ls *.mp4); do
    out=$(ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0 $_name)
    width=$(echo $out | cut -d x -f 1)
    height=$(echo $out | cut -d x -f 2)
    echo -e $_name = $width x $height
    # if [ $width -ge 1000 ]; then
    #    ffmpeg -i $_name -vf scale=iw/2:ih/2 $(echo $_name | sed -e 's/\.mp4//')_resize.mp4
    #    rm $_name
    # fi
done
