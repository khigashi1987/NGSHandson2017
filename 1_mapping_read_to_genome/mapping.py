#!/usr/bin/env python

import os
import logging
from hiclib import mapping
from mirnylib import h5dict, genome

logging.basicConfig(level=logging.DEBUG)

if not os.path.exists('../data/tmp'):
    os.mkdir('../data/tmp')

# Map the reads iteratively.
mapping.iterative_mapping(
    bowtie_path='/usr/bin/bowtie2',
    bowtie_index_path='../Index/hg19',
    fastq_path='../data/SRR1658595_10M_1.fastq',
    out_sam_path='../data/SRR1658595_10M_1.bam',
    min_seq_len=25,
    len_step=5,
    seq_start=0,
    seq_end=35,
    nthreads=2,
    temp_dir='../data/tmp',
    bowtie_flags='--very-sensitive')

mapping.iterative_mapping(
    bowtie_path='/usr/bin/bowtie2',
    bowtie_index_path='../Index/hg19',
    fastq_path='../data/SRR1658595_10M_2.fastq',
    out_sam_path='../data/SRR1658595_10M_2.bam',
    min_seq_len=25,
    len_step=5,
    seq_start=0,
    seq_end=35,
    nthreads=2,
    temp_dir='../data/tmp',
    bowtie_flags='--very-sensitive')
