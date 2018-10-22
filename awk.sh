#!/bin/bash

echo 0=$(awk '$3 ~ /0/ {print $0}' $1 | wc -l)
echo 1=$(awk '$3 ~ /1/ {print $0}' $1 | wc -l)

echo train_0=$(awk '$4 ~ /train/ && $3 ~ /0/ {print $0}' $1 | wc -l)
echo val_0=$(awk '$4 ~ /val/ && $3 ~ /0/ {print $0}' $1 | wc -l)

echo train_1=$(awk '$4 ~ /train/ && $3 ~ /1/ {print $0}' $1 | wc -l)
echo val_1=$(awk '$4 ~ /val/ && $3 ~ /1/ {print $0}' $1 | wc -l)
