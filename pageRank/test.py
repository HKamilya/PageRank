import json
import math
import sys

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

fname = 'data3.json'


def load(file_name):
    G = nx.MultiDiGraph()
    d: dict = json.load(open(file_name))
    for link, links in d.items():
        for link__ in links:
            link__: dict
            for link1, links1 in link__.items():
                link1: str
                G.add_edge(link, link1)
                for link2__ in links1:
                    for link3, links3 in link2__.items():
                        G.add_edge(link1, link3)
                        for link___ in links3:
                            G.add_edge(link3, link___)

    plt.figure(figsize=(40, 40))
    # nx.draw_networkx(G, node_color='green')
    options = {
        'node_color': 'red',
        'node_size': 10,
        'edge_color': 'blue',
        'width': 0.08
    }
    nx.write_gml(G, 'remote.gml')

    nx.draw_random(G, with_labels=False, **options)
    # plt.show()
    plt.savefig('foo.png')

    # print(d.items())
    #
    # G.add_nodes_from(d['nodes'])
    # G.add_edges_from(d['edges'])
    # return G


# load(fname)

def load_grapth():
    import numpy as np
    # np.set_printoptions(threshold=sys.maxsize)
    G = nx.read_gml('remote.gml')
    A = nx.adjacency_matrix(G)
    print(A / A.sum(axis=0))
    B = A / A.sum(axis=0)
    np.savetxt('array.out', B)


def matrix():
    x = a = np.matrix('1 2 1; 3 4 5')
    print(x)
    x: np.matrix

    a, b = x.shape
    print(a, b)


def float_to_mini_float():
    a = 3.811258289353455e-48
    b = round(a, 50)
    print(b)


def sort_terst():
    a = np.array([5, 2, 3])
    b = np.sort(a)
    print(b)
    c = np.argsort(a)
    print(c)

def array_game():
    a= [1,2,3,4,5,6,7,8,9,10,11,12,13]
    print(a[-5:])

# float_to_mini_float()

# sort_terst()
array_game()
# matrix()
# load_grapth()
