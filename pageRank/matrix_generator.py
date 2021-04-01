import networkx as nx
import numpy as np

np.seterr(divide='ignore', invalid='ignore')


def matrix_from_graph():
    G = nx.read_gml('remote.gml')

    A = nx.adjacency_matrix(G)

    B = (A / A.sum(axis=0))
    B = np.nan_to_num(B, nan=0)

    # G_LIST = list(list(G.edges())[0][-1].keys())
    # print(G_LIST)
    G_LIST = G.nodes()

    B.tofile('matrix.out', sep=' ')

    height, width = B.shape
    print(height, width)

    return B, height, width,G_LIST


if __name__ == '__main__':
    matrix_from_graph()
