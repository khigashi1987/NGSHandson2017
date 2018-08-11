#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
#
# Author:   HIGASHI Koichi
# Created:  2017-08-23
#

import sys
import numpy as np
import networkx as nx
import itertools

def main(matfile):
    outfilename = 'dist.npy'
    mat = np.loadtxt(matfile)
    Nodes = range(mat.shape[0])
    n_nodes = len(Nodes)
    print 'Number of nodes:', n_nodes
    G = nx.Graph()
    G.add_nodes_from(Nodes)
    for i,j in itertools.combinations(Nodes, 2):
        if mat[i, j] != 0.0:
            G.add_edge(i, j, weight = 1. / mat[i,j])
    isolated_nodes = []
    for i, component in enumerate(nx.connected_components(G)):
        if len(component) == 1:
            isolated_nodes.append(list(component)[0])
    n_isolated_nodes = len(isolated_nodes)
    n_connected_nodes = n_nodes - n_isolated_nodes
    print '\tIsolated nodes:', n_isolated_nodes
    # remove isolated_nodes
    mat_mask = np.ones(mat.shape).astype(bool)
    mat_mask[np.array(isolated_nodes), :] = False
    mat_mask[:, np.array(isolated_nodes)] = False
    mat = mat[mat_mask].reshape((n_connected_nodes, n_connected_nodes))
    # reconstruct graph
    Nodes = range(mat.shape[0])
    G = nx.Graph()
    G.add_nodes_from(Nodes)
    for i,j in itertools.combinations(Nodes, 2):
        if mat[i, j] != 0.0:
            G.add_edge(i, j, weight = 1. / mat[i,j])
    # convert into distance matrix
    print 'converting...'
    dist_mat = np.zeros(mat.shape).astype(float)
    for i,j in itertools.combinations(Nodes, 2):
        shortest_path_length = nx.shortest_path_length(G, source=i, target=j, weight='weight')
        dist_mat[i, j] = shortest_path_length
        dist_mat[j, i] = shortest_path_length
    np.save(outfilename, dist_mat)
    print 'done.'

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'usage: python %s contact_matrix_file' % sys.argv[0]
        exit()
    main(sys.argv[1])
