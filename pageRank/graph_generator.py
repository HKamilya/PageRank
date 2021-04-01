import networkx as nx
import matplotlib.pyplot as plt


def generator_by_json(d):
    G = nx.MultiDiGraph()
    for link, links in d.items():
        for link__ in links:
            for link1, links1 in link__.items():
                G.add_edge(link, link1)
                for link2__ in links1:
                    for link3, links3 in link2__.items():
                        G.add_edge(link1, link3)
                        for link___ in links3:
                            G.add_edge(link3, link___)

    plt.figure(figsize=(50, 50))
    options = {
        'node_color': 'red',
        'node_size': 12,
        'edge_color': 'blue',
        'width': 0.07
    }
    print('q')



    nx.write_gml(G, 'remote.gml')

    nx.draw_random(G, with_labels=False, **options)
    plt.savefig('foo.png')
    # try:
    #     plt.show()
    # except:
    #     pass


if __name__ == '__main__':
    # dataqqq.json
    import json

    with open('dataqqq.json') as json_file:
        data = json.load(json_file)
    generator_by_json(data)
