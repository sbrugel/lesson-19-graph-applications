import networkx as nx
import matplotlib.pyplot as plt


def find_exam_schedule(graph: nx.DiGraph, course_id: str):
    try:
        colors = {}
        # Breadth-first search with coloring for exam schedule
        bfs_tree = nx.bfs_tree(graph, course_id)
        for node in bfs_tree:
            avail_colors = set(range(len(graph)))
            for neighbor in graph.neighbors(node):
                if neighbor in colors:
                    avail_colors.discard(colors[neighbor])
            # Choose the first available color for the node
            colors[node] = min(avail_colors)

        for exam, color in colors.items():
            print(f"{exam}: Day {color+1}")

    except KeyError:
        print('ERROR: Invalid exam supplied.')

src_exam = 'A'

G = nx.Graph()

# add the 20 exam nodes
exams = "A61 B63 C74 D65 E64 F15 G45 H85 I82 J35 K36 L41 M52 N26 O27 P81 Q83 R86 S75 T35".split(' ')
for exam in exams:
    G.add_node(exam[0], pos = (int(exam[1]), int(exam[2])))

edges = "AB AC BD BA DF DB FH FD FI FJ FK GH HG HI HK IJ IF IM JK JL LO IN IM NO NP ON LQ PQ QR QP RS RT SR TR ST TS".split()
for edge in edges:
    G.add_edge(edge[0], edge[1])

find_exam_schedule(G, src_exam)

node_positions = nx.get_node_attributes(G, 'pos')
edge_weights = nx.get_edge_attributes(G, 'weight')

nx.draw_networkx_nodes(G, pos=node_positions)
nx.draw_networkx_labels(G, pos=node_positions, font_color='white', font_size=11, font_weight='bold')
nx.draw_networkx_edges(G, pos=node_positions)
nx.draw_networkx_edge_labels(G, pos=node_positions, edge_labels=edge_weights)
plt.show()