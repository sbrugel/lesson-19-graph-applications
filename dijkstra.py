import networkx as nx
import matplotlib.pyplot as plt

# algorithm to find the shortest paths from a source to all other nodes
def find_shortest_paths(graph: nx.Graph, source: str, nodes: list[str]):
    try:
        length, path = nx.single_source_dijkstra(graph, source)
        for node in nodes:
            print(f"{node}: {length[node]}")
    except KeyError:
        print('Error: Invalid building supplied.')

# create a new undirected Graph
G = nx.Graph()

# add the 20 building nodes
    # string of node-xpos-ypos
buildings = "A61 B63 C74 D65 E64 F15 G45 H85 I82 K36 L41 M52 N26 O27 P81 R84 S75 T35 U25 W66".split(' ')
for building in buildings:
    G.add_node(building[0], pos = (int(building[1]), int(building[2])))

# add the 26 weighted, undirected edges
    # string of node1-node2-weight
edges = "AL7 AM4 AP2 BC2 BE3 BG5 BM2 CI3 CR1 CS1 DE2 DG1 DW3 FU1 GT2 GW3 HR4 HS3 IP4 IR3 KN2 KT2 LM3 NO5 NU2 TU2".split(' ')
for edge in edges:
    G.add_edge(edge[0], edge[1], weight = int(edge[2]))

# find the shortest path from McDowell Hall (O) to each other building
nodes = [building[0] for building in buildings]
find_shortest_paths(G, 'O', nodes)

# generate and display the graph
node_positions = nx.get_node_attributes(G, 'pos')
edge_weights = nx.get_edge_attributes(G, 'weight')

nx.draw_networkx_nodes(G, pos=node_positions)
nx.draw_networkx_labels(G, pos=node_positions, font_color='white', font_size=11, font_weight='bold')
nx.draw_networkx_edges(G, pos=node_positions)
nx.draw_networkx_edge_labels(G, pos=node_positions, edge_labels=edge_weights)
plt.show()