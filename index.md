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
```

## Python Environment Setup

```python
import networkx as nx
```

# Depth-First Search: Course Curriculum Paths

**We are given the course catalog of UD's Computer Science AI Concentration, consisting of all "core" courses and a few extra electives. Given this catalog, written as a directed graph with edges representing requirements to classes they satisfy, use depth-first search to find all possible paths from one specified course to another.**:

> **Formal Description**:
>
> - Input:
> - Output:

**Graph Problem/Algorithm**: [DFS]

**Setup code**:

```python

```

**Visualization**:

![Image goes here](Relative image filename goes here)

**Solution code:**

```python

```

**Output**

```

```

**Interpretation of Results**:

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
> - Input: A text file formatted as an adjaceny matrix, splitting up each edge 
> by commas. 
> 
> 
>   Example:  
> 
> 0, 0, 3, 2,  
> 0, 0, 4, 2,  
> 3, 4, 0, 2,   
> 2, 2, 2, 0, 
> 
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
