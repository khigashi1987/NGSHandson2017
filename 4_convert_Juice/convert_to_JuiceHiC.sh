#!/bin/sh
cat ./forJuice.txt | sort -k2,2d -k6,6d -n | uniq | nl -n ln | tr "\t" " " > ./forJuice_sorted.txt
sh /home/manager/HiC/src/juicebox.for.review.archive/juicebox pre ./forJuice_sorted.txt test.hic hg19
