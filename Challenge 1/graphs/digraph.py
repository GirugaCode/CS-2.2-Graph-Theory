#!python3
"""
Implementation of a directed Graph Class
"""
        
class Digraph:
    def __init__(self):
        """ 
        Initializes a graph object with an empty dictionary.
        self.edge_list -> List of the edges
        self.num_verticies -> List of verticies
        """
        # These represents the edges
        self.edge_list = {}
        self.num_verticies = 0