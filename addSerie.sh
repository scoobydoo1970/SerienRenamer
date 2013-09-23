#!/bin/sh

von=$1
nach=$2

cat $von | cut -f1,4 | sed -e 's/1x/S01E/g;s/2x/S02E/g;s/3x/S03E/g;s/4x/S04E/g;s/5x/S05E/g;s/6x/S06E/g;s/7x/S07E/g;s/8x/S08E/g;s/9x/S09E/g;s/10x/S10E/g;s/11x/S11E/g;'> $nach
