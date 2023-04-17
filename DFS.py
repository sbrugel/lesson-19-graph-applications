import networkx as nx
import matplotlib.pyplot as plt

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
G.add_edge('CISC 108', 'CISC 181') # add nodes & edges
G.add_edge('CISC 108', 'CISC 210')
G.add_edge('CISC 210', 'CISC 220')
G.add_edge('CISC 210', 'CISC 260')
G.add_edge('CISC 181', 'CISC 275')
G.add_edge('CISC 220', 'CISC 275')
G.add_edge('CISC 220', 'CISC 303')
G.add_edge('CISC 220', 'CISC 304')
G.add_edge('CISC 220', 'CISC 320')
G.add_edge('CISC 220', 'CISC 361')
G.add_edge('CISC 260', 'CISC 361')
G.add_edge('CISC 220', 'CISC 372')
G.add_edge('CISC 260', 'CISC 372')
G.add_edge('CISC 220', 'CISC 437')
G.add_edge('CISC 220', 'CISC 442')
G.add_edge('CISC 275', 'CISC 474')
G.add_edge('CISC 220', 'CISC 481')
G.add_edge('CISC 304', 'CISC 481')
G.add_edge('CISC 220', 'CISC 483')
G.add_edge('CISC 220', 'CISC 484')
G.add_edge('CISC 275', 'CISC 498')
G.add_edge('CISC 498', 'CISC 499')
G.add_edge('CISC 320', 'CISC 499')
G.add_edge('MATH 241', 'MATH 210')
G.add_edge('MATH 210', 'MATH 205')
G.add_edge('MATH 210', 'CISC 303')
G.add_edge('MATH 210', 'CISC 304')
G.add_edge('MATH 210', 'CISC 320')
G.add_edge('MATH 205', 'CISC 483')
G.add_edge('MATH 205', 'CISC 484')

# other edges, based on the recommended path, not necessarily requirements
G.add_edge('MATH 241', 'CISC 181')
G.add_edge('MATH 241', 'CISC 210')
G.add_edge('CISC 181', 'CISC 220')
G.add_edge('CISC 181', 'CISC 260')
G.add_edge('CISC 220', 'CISC 355')
G.add_edge('CISC 481', 'CISC 483')
G.add_edge('CISC 483', 'CISC 484')
G.add_edge('CISC 361', 'CISC 372')

# FOR A WEIGHTED GRAPH
# G.add_weighted_edges_from([('CISC 108', 'CISC 181', 1)]) # add nodes & edges

# draw the graph and show it MUST BE THE LAST TWO LINES
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()