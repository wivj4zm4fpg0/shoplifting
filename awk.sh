#!/bin/bash

echo 0=$(awk '$3 ~ /0/ {print $0}' $1 | wc -l)
echo 1=$(awk '$3 ~ /1/ {print $0}' $1 | wc -l)
