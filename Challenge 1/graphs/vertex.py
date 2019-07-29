#!python3
"""
Implementation of a Vertex that can be used for a Graph
"""

class Vertex:
    def __init__(self, vertex):
        """ 
        Initializes the vertex class
        self.id -> Int
        self.neighbors -> Dictionary
        """
        self.id = vertex
        self.neighbors = {}

    def add_neighbor(self, vertex, weight=0):
        """add a neighbor along a weighted edge"""
        if vertex not in self.neighbors:
            self.neighbors[vertex] = weight

    def get_neighbors(self):
        """return the neighbors of this vertex"""
        return self.neighbors

    def get_id(self):
        """return the id of this vertex"""
        return self.id