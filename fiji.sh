#!/usr/bin/bash -l

echo "Loading fiji module"
#module load fiji/20170530-java-1.8.0_121
module load fiji/20170530
module load cuda/9.2.88-gcc-7.3.0-2.30
module load ffmpeg/4.1-foss-2018b

$EBROOTFIJI/ImageJ-linux64 &

wait $!

