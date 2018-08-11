#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

from mirnylib import genome
from mirnylib import h5dict
from mirnylib import plotting
from hiclib import binnedData

genome_db = genome.Genome('../Ref/hg19', readChrms=['#','X'])

raw_heatmap = h5dict.h5dict('../2_filtering_reads/heatmap-res-1M.hdf5', mode='r')
resolution = int(raw_heatmap['resolution'])

BD = binnedData.binnedData(resolution, genome_db)
BD.simpleLoad('../2_filtering_reads/heatmap-res-1M.hdf5', 'Rao2014_10M')

#BD.removeDiagonal()
BD.removeBySequencedCount(0.5)
BD.removePoorRegions(cutoff=1)
BD.truncTrans(high=0.0005)
BD.iterativeCorrectWithoutSS()

BD.export('Rao2014_10M', './IC-heatmap-res-1M.hdf5')

fig = plt.figure()
plotting.plot_matrix(np.log(BD.dataDict['Rao2014_10M']+1.0))
fig.savefig('./heatmap.pdf')

'''
print 'Eigendecomposition...'
BD.removeCis()
BD.fakeCis()
BD.removeZeros()
BD.doEig(numPCs=1) # first principal component
BD.restoreZeros(value=0)
eigenvectors = BD.EigDict['Rao2014_10M']
print eigenvectors[:,:10]
np.savetxt('egvecs.txt', eigenvectors)
'''
