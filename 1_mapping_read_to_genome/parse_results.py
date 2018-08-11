#!/usr/bin/env python

import logging
from hiclib import mapping
from mirnylib import h5dict, genome

logging.basicConfig(level=logging.DEBUG)

mapped_reads = h5dict.h5dict('./mapped_reads.hdf5')
genome_db = genome.Genome('../Ref/hg19', readChrms=['#','X'])

mapping.parse_sam(
    sam_basename1='../data/SRR1658595_10M_1.bam',
    sam_basename2='../data/SRR1658595_10M_2.bam',
    out_dict=mapped_reads,
    genome_db=genome_db,
    enzyme_name='MboI')
