#!/usr/bin/env python

from mirnylib import genome
from hiclib import fragmentHiC

genome_db = genome.Genome('../Ref/hg19', readChrms=['#','X'])
genome_db.setEnzyme('MboI')

fragments = fragmentHiC.HiCdataset(
    filename='./fragment_dataset.hdf5',
    genome=genome_db,
    maximumMoleculeLength=500,
    mode='w')

fragments.parseInputData(
    dictLike='../1_mapping_read_to_genome/mapped_reads.hdf5')

fragments.filterRsiteStart(offset=5)
fragments.filterDuplicates()

fragments.filterLarge()
fragments.filterExtreme(cutH=0.005, cutL=0)

fragments.saveHeatmap('./heatmap-res-1M.hdf5', resolution=1000000)
fragments.printMetadata(saveTo='./statistics.txt')
