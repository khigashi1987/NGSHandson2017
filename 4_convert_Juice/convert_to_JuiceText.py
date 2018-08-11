#!/usr/bin/env python

from itertools import repeat

from mirnylib import genome
from mirnylib import h5dict
from hiclib import fragmentHiC

target_chromosome = 1

genome_db = genome.Genome('../Ref/hg19', readChrms=['#','X'])
genome_db.setEnzyme('MboI')

fragments = fragmentHiC.HiCdataset(
    filename='./tmp',
    genome=genome_db,
    maximumMoleculeLength=500,
    mode='w')
fragments.load('../2_filtering_reads/fragment_dataset.hdf5')

juicefile = './forJuice.txt'
with open(juicefile, 'w') as f:
    for str1, str2, chr1, chr2, pos1, pos2, mapq in zip(fragments.h5dict['strands1'], fragments.h5dict['strands2'], fragments.h5dict['chrms1'], fragments.h5dict['chrms2'], fragments.h5dict['cuts1'], fragments.h5dict['cuts2'], repeat(32)):
        if chr1+1 == target_chromosome and chr2+1 == target_chromosome:
           chr1 = str(chr1+1) if chr1<23 else 'X'
           chr2 = str(chr2+1) if chr2<23 else 'X'
           frag1 = 0 # not used
           frag2 = 1 # not used
           str1 = int(str1) - 1
           str2 = int(str2) - 1
           f.write('\t'.join([str(i) for i in (str1, chr1, pos1, frag1, str2, chr2, pos2, frag2, int(mapq), int(mapq))]) + '\n')
