#!/bin/sh

I=8
START=$(date +%s)

python3 hetmans.py $I

END=$(date +%s)
DIFF=$(( $END -$START))

maxtime=5

while [ $DIFF -lt $maxtime ] 
do
I=$((I+1))

START=$(date +%s)

python3 hetmans.py $I

END=$(date +%s)
DIFF=$(( $END - $START))

done

echo $I

