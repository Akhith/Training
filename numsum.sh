#! /bin/bash 
sum=0
if [ "$#" -lt 1 ] ; then
    echo Usage: $0 args
    exit 1
fi
grep -o -E '[0-9]+' $@ > result
awk '{sum += $1} END {print sum}' result
