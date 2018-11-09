#!/bin/bash -eu

function usage() {
cat <<__EOT__

動画をmp4に変換するスクリプト。
引数に動画群が入ったディレクトリを指定してください。
例: ./mp4.sh video_dir

__EOT__
}

if [[ $# -ne 1 ]]; then
    usage
    exit 1
fi

cd $1

for _video in $(ls); do
    if ! echo ${_video} | grep -q ".mp4"; then
        _name=$(echo ${_video} | sed -e 's/\..*$//g').mp4
        ffmpeg -i ${_video} -y -strict -2 ${_name}
    fi
done
