import networkx as nx
import matplotlib.pyplot as plt

def find_requirements(graph: nx.DiGraph, course_id: str):
    try:
        dfs_from_source = nx.dfs_edges(G, source=src_course)
        for edge in dfs_from_source:
            print(edge)
    except KeyError:
        print('ERROR: Invalid course ID supplied.')

src_course = 'CISC 304'

G = nx.DiGraph() # create a new Graph
G.add_node('CISC 108') # add nodes & edges
G.add_node('CISC 181')
G.add_node('CISC 210')
G.add_node('CISC 220')
G.add_node('CISC 260')
G.add_node('CISC 275')
G.add_node('CISC 303')
G.add_node('CISC 304')
G.add_node('CISC 320')
G.add_node('CISC 355')
G.add_node('CISC 361')
G.add_node('CISC 372')
G.add_node('CISC 437')
G.add_node('CISC 442')
G.add_node('CISC 474')
G.add_node('CISC 481')
G.add_node('CISC 483')
G.add_node('CISC 484')
G.add_node('CISC 498')
G.add_node('CISC 499')
G.add_node('MATH 241')
G.add_node('MATH 210')
G.add_node('MATH 205')

# direct requirements get a single directed edge
G.add_edge('CISC 181', 'CISC 108') # add nodes & edges
G.add_edge('CISC 210', 'CISC 108')
G.add_edge('CISC 220', 'CISC 210')
G.add_edge('CISC 260', 'CISC 210')
G.add_edge('CISC 275', 'CISC 181')
G.add_edge('CISC 275', 'CISC 220')
G.add_edge('CISC 303', 'CISC 220')
G.add_edge('CISC 304', 'CISC 220')
G.add_edge('CISC 320', 'CISC 220')
G.add_edge('CISC 361', 'CISC 220')
G.add_edge('CISC 361', 'CISC 260')
G.add_edge('CISC 372', 'CISC 220')
G.add_edge('CISC 372', 'CISC 260')
G.add_edge('CISC 437', 'CISC 220')
G.add_edge('CISC 442', 'CISC 220')
G.add_edge('CISC 474', 'CISC 220')
G.add_edge('CISC 481', 'CISC 220')
G.add_edge('CISC 481', 'CISC 304')
G.add_edge('CISC 483', 'CISC 220')
G.add_edge('CISC 484', 'CISC 220')
G.add_edge('CISC 498', 'CISC 275')
G.add_edge('CISC 499', 'CISC 498')
G.add_edge('CISC 499', 'CISC 320')
G.add_edge('MATH 210', 'MATH 241')
G.add_edge('MATH 205', 'MATH 210')
G.add_edge('CISC 303', 'MATH 210')
G.add_edge('CISC 304', 'MATH 210')
G.add_edge('CISC 320', 'MATH 210')
G.add_edge('CISC 483', 'MATH 205')
G.add_edge('CISC 484', 'MATH 205')

# other edges, based on the recommended path, not necessarily requirements
G.add_edge('CISC 181', 'MATH 241')
G.add_edge('CISC 210', 'MATH 241')
G.add_edge('CISC 220', 'CISC 181')
G.add_edge('CISC 260', 'CISC 181')
G.add_edge('CISC 355', 'CISC 220')
G.add_edge('CISC 483', 'CISC 481')
G.add_edge('CISC 484', 'CISC 483')
G.add_edge('CISC 372', 'CISC 361')

# FOR A WEIGHTED GRAPH
# G.add_weighted_edges_from([('CISC 108', 'CISC 181', 1)]) # add nodes & edges

find_requirements(G, src_course)

# draw/show graph
nx.draw(G, pos=nx.circular_layout(G), with_labels=True, font_weight='bold')
plt.show()