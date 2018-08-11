#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
#
# Author:   HIGASHI Koichi
# Created:  2017-08-23
#

import numpy as np
from sklearn import manifold
import seaborn as sns
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
sns.set(style='whitegrid')

mat = np.load('./dist.npy')
print 'MDS computation...'
mds = manifold.MDS(n_components=3, max_iter=1000, dissimilarity='precomputed')
coords = mds.fit_transform(mat)

fig = plt.figure(figsize=(16,12))
ax = fig.add_subplot(111, projection='3d')
colors = sns.color_palette('jet_r', coords.shape[0])
ax.plot(coords[:,0], coords[:,1], coords[:,2], color='gray', linestyle=':')
ax.scatter(coords[:,0], coords[:,1], coords[:,2], c=colors, marker='o', s=500, alpha=0.7)
plt.show()
