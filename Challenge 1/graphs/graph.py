#!python3
from graphs.vertex import Vertex

class Graph:
    def __init__(self):
        """ 
        Initializes a graph object with an empty dictionary.
        self.edge_list -> List of the edges
        self.num_verticies -> List of verticies
        """
        # These represents the edges
        self.edge_list = {}
        self.num_verticies = 0