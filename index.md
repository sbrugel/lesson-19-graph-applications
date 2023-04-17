# Campus Life & Graphing

**CISC320 Spring 2023 Lesson 14 - Graph Applications**

Group Members:

- Simon Brugel (sbrugel@udel.edu)
- Aman Singh (amans@udel.edu)
- Ryan Sanchez (ryansan@udel.edu)
- Gavin Caulfield (gavcaul@udel.edu)

Description of project

## Installation Code

```sh
$> pip install networkx
$> pip install matplotlib
```

## Python Environment Setup

```python
import networkx as nx
import matplotlib.pyplot as plt
```

# Depth-First Search: Finding Course Prerequisites

**We are given the course catalog of UD's Computer Science AI Concentration, consisting of all "core" courses and a few extra electives. Given this catalog, written as a directed graph with edges connecting classes to their prerequisites (as well as certain "recommended" classes), as well as a string containing a course ID, use depth-first search to list ALL classes one needs to take to be able to take this class. For example, CISC 220 requires 210, which requires 108, and strongly recommends 181. CISC 210 also requires MATH 241. So CISC 108, CISC 181, MATH 241, and CISC 210 will be listed as required courses.**:

> **Formal Description**:
>
> - Input: A directed graph, consisting of courses and edges as specified above (type: nx.DiGraph); a valid course ID (i.e. 'CISC 481') (type: str).
> - Output: A list of the edges that were traversed from that course, using depth first search (type: generator).

**Graph Problem/Algorithm**: [DFS]

**Setup code**:

```python
src_course = 'CISC 481'

G = nx.DiGraph() # create a new Graph
G.add_node('CISC 108') # add nodes
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
G.add_edge('CISC 181', 'CISC 108') # add edges
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

find_requirements(G, src_course) # implementation details below.
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()
```

**Visualization**:

![Image goes here](Relative image filename goes here)

**Solution code:**

```python
def find_requirements(graph: nx.DiGraph, course_id: str):
    try:
        dfs_from_source = nx.dfs_edges(G, source=src_course)
        for edge in dfs_from_source:
            print(edge)
    except KeyError:
        print('ERROR: Invalid course ID supplied.')
```

**Output**

```
('CISC 481', 'CISC 220')
('CISC 220', 'CISC 210')
('CISC 210', 'CISC 108')
('CISC 210', 'MATH 241')
('CISC 220', 'CISC 181')
('CISC 481', 'CISC 304')
('CISC 304', 'MATH 210')
```

**Interpretation of Results**:

The course requirements for CISC 481 are as follows:

- CISC 220 (direct requirement)
- CISC 210 (needed for 220)
- CISC 108 (needed for 210)
- MATH 241 (needed for 210)
- CISC 181 (needed for 220)
- CISC 304 (direct requirement)
- MATH 210 (needed for 304)

# Minimum Distance to Check Every Blue Light

**Informal Description**:
Many college campuses, including UD, have blue safety lights
all across campus, which when press will connect you with the police.
However, every year, these are required to be checked to ensure functionality.
As said before, these are all across campus, and checking every single one would require
a lot of time and energy. We want to find a path/way to hit every single blue light in the
least amount of distance travelled.

> **Formal Description**:
>
> - Input: A text file formatted as an adjacency matrix, splitting up each edge
>   by commas.
>
>   Example:
>
> 0, 0, 3, 2,  
> 0, 0, 4, 2,  
> 3, 4, 0, 2,  
> 2, 2, 2, 0,
>
> - Output: A Minimum Spanning Tree and a printed picture of said Tree

**Graph Problem/Algorithm**: [MST]

**Setup code**:

```python
import matplotlib.pyplot as plt
if __name__ == "__main__":

    G = nx.Graph()
    with open('path.txt') as f:
        x = 1
        for line in f:
            values = line.strip().split(",")
            for y, value in enumerate(values, start=1):
                if value.strip().isnumeric() and int(value) != 0:
                    G.add_edge(x, y, weight=int(value))
            x += 1

```

**Visualization**:

![Sample Graph for the Blue Lights Problem](Figure_1.png)

**Solution code:**

```python
    G = nx.minimum_spanning_tree(G, weight='weight', algorithm='prim', ignore_nan=False)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.show()

```

**Output**
![The Minimum Spanning Tree for the Blue Lights](Figure_2.png)

**Interpretation of Results**:
If you follow the path/tree shown, you will visit every blue light while
traveling the least distance possible.
