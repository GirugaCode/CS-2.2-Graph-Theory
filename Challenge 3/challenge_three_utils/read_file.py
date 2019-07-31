#!python3
"""
Reads the graph-data.txt file and stores the information
"""

from graphs.digraph import Digraph
from graphs.graph import Graph
from graphs.vertex import Vertex

def read_file(text_file):
    graph = Graph()
    verts = []
    edges = []
    is_weighted = None

    with open(text_file, "r") as open_file:
        line_counter = 0
        for line in open_file:
            if line_counter == 0: # Chooses either a Graph or Digraph
                graph_type = line.strip()
                if graph_type == "G":
                    graph = Graph()
                elif graph_type == "D":
                    graph = Digraph()
                else:
                    raise ValueError("A Graph type has not been properly specified")
            if line_counter == 1: # Adds all the Verticies from the txt file
                for key in line.strip().split(","):
                    verts.append(key)
            elif line_counter > 1: # Add all the edges and checks if its weighted
                edge = line.strip("()\n").split(",")
                if is_weighted is None:
                    is_weighted = bool(len(edge) == 3)
                elif is_weighted and len(edge) < 3:
                    raise ValueError("All edges must be either unweighted or weighted")

                if len(edge) != 3 and len(edge) != 2:
                    raise ValueError(f"Text file has unusual amount of arguments for edges")
                if len(edge) > 3:
                    raise ValueError("To many arguments for the edges")
                edges.append(edge)
            line_counter += 1 # Traverses through the txt file line by line 

        return graph, verts, edges