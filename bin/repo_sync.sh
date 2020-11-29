#!/bin/sh
repo sync --no-tags -j 24
while [ $? -ne 0 ]
do
repo sync --no-tags  -j 24
done
