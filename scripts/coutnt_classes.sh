#!/bin/bash

FILE=$1

function usage() {
cat <<__EOT__

cvsファイルからクラス数の割合や訓練データとテストデータの割合を求める。
引数に動画情報が入ったディレクトリを指定してください。
例: ./awk.sh hoge.cvs

__EOT__
}

while getopts :h-: OPT; do
    case ${OPT} in
        -)
            case $OPTARG in
                help)
                    usage
                    exit 0
                    ;;
                *)
                    usage
                    exit 1
                    ;;
            esac
            ;;
        h)
            usage
            exit 0
            ;;
        *)
            usage
            exit 1
            ;;
    esac
done

if [ $# -lt 1 ]; then
    usage
    exit 1
fi

# クラス数をカウント
echo 0=$(awk '$3 ~ /0/ {print $0}' ${FILE} | wc -l)
echo 1=$(awk '$3 ~ /1/ {print $0}' ${FILE} | wc -l)

# 非・万引きクラスの訓練データとテストデータの数をカウント
echo train_0=$(awk '$4 ~ /train/ && $3 ~ /0/ {print $0}' ${FILE} | wc -l)
echo validation_0=$(awk '$4 ~ /validation/ && $3 ~ /0/ {print $0}' ${FILE} | wc -l)

# 万引きクラスの訓練データとテストデータの数をカウント
echo train_1=$(awk '$4 ~ /train/ && $3 ~ /1/ {print $0}' ${FILE} | wc -l)
echo validation_1=$(awk '$4 ~ /validation/ && $3 ~ /1/ {print $0}' ${FILE} | wc -l)
