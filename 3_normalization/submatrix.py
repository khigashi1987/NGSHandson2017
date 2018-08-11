#!/usr/bin/env python

import numpy as np
from mirnylib import h5dict

normalized_matrix = h5dict.h5dict('./IC-heatmap-res-1M.hdf5', mode='r')
target_chromosome = 19
chromosome_mask = normalized_matrix['chromosomeIndex'] == (target_chromosome - 1)
target_matrix = normalized_matrix['heatmap'][chromosome_mask,:][:,chromosome_mask]
np.savetxt('./norm_mat.txt', target_matrix)
