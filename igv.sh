#!/usr/bin/bash -l

echo "Loading igv module"
#module load igv/2.4.6-java-1.8.0_121
module load igv/2.5.0-java-11

$EBROOTIGV/igv.sh &
