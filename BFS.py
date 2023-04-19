import networkx as nx
import matplotlib.pyplot as plt


def find_exam_schedule(graph: nx.DiGraph, course_id: str):
    try:
        bfs_from_source = nx.dfs_edges(G, source=src_exam)
        for edge in bfs_from_source:
            print(edge)
    except KeyError:
        print('ERROR: Invalid exam supplied.')

src_exam = 'A'

G = nx.Graph()

# add the 20 exam nodes
exams = "A61 B63 C74 D65 E64 F15 G45 H85 I82 J35 K36 L41 M52 N26 O27 P81 Q83 R86 S75 T35".split(' ')
for exam in exams:
    G.add_node(exam[0], pos = (int(exam[1]), int(exam[2])))

conflicts = "AB AC BD BA DF DB FH FD FI FJ FK GH HG HI HK IJ IF IM JK JL LO IN IM NO NP ON LQ PQ QR QP RS RT SR TR ST TS".split()
for conflict in conflicts:
    G.add_edge(conflict[0], conflict[1])

find_exam_schedule(G, src_exam)

node_positions = nx.get_node_attributes(G, 'pos')
edge_weights = nx.get_edge_attributes(G, 'weight')

nx.draw_networkx_nodes(G, pos=node_positions)
nx.draw_networkx_labels(G, pos=node_positions, font_color='white', font_size=11, font_weight='bold')
nx.draw_networkx_edges(G, pos=node_positions)
nx.draw_networkx_edge_labels(G, pos=node_positions, edge_labels=edge_weights)
plt.show()