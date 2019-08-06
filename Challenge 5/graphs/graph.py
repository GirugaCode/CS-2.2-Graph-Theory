#!python3
from graphs.vertex import Vertex

class Graph:
    def __init__(self):
        """ 
        Initializes a graph object with an empty dictionary.
        self.vert_dict -> List of the edges
        self.num_verticies -> List of verticies
        """
        self.vert_dict = {}
        self.num_verticies = 0
        self.num_edges = 0

    def add_vertex(self, key):
        """
        Add a new vertex object to the graph with 
        the given key and return the vertex. 
        """
        self.num_verticies += 1
        new_vertex = Vertex(key)
        self.vert_dict[key] = new_vertex
        return new_vertex

    def add_edge(self, f, t, cost=0):
        """add an edge from vertex f to vertex t with a cost"""
        if f not in self.vert_dict:
            self.add_vertex(f)
        if t not in self.vert_dict:
            self.add_vertex(t)
        self.vert_dict[f].add_neighbor(self.vert_dict[t], cost)
        self.vert_dict[t].add_neighbor(self.vert_dict[f], cost)
        self.num_edges += 1

    def get_vertices(self):
        """return all the vertices in the graph"""
        return self.vert_dict.keys()

    def get_edges(self, vertex):
        """ Returns all the edges of a given vertex"""
        dict_edges = self.vert_dict[vertex].neighbors
        return dict_edges

    def is_eulerian(self):
        """ Determines if a graph has a Eulerian Cycle """
        odd = 0 # Keeps track of the mod value for every degree of each verticies
        for vertex in self.vert_dict:
            if len(self.get_edges(vertex)) % 2 != 0: # Compares the modded amounts of degrees to 0
                odd += 1 # Increment tracker
        if odd == 0: # Conditionals
            return True
        else:
            return False

    def __iter__(self):
        """iterate over the vertex objects in the
        graph, to use sytax: for v in g
        """
        return iter(self.vert_dict.values())