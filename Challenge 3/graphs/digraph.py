#!python3
"""
Implementation of a directed Graph Class
"""
from graphs.vertex import Vertex

class Digraph:
    def __init__(self):
        """ 
        Initializes a graph object with an empty dictionary.
        self.edge_list -> List of the edges
        self.num_verticies -> Number of verticies
        self.num_edges -> Number of edges
        """
        # These represents the edges
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
        dict_edges = self.vert_dict[vertex].neighbors
        return dict_edges

    def _dfs_recursive(self, from_vert, to_vert, visited):
        """
        Resources: https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
        """

        # Error handling to make sure that both the vertices are in the graph
        if from_vert not in self.vert_dict or to_vert not in self.vert_dict:
            raise KeyError("Either or both of the keys are not in the graph!")

        if visited is None:
            visited = set()

        curr_vert = self.vert_dict[from_vert]
        visited.add(from_vert)

        for neighbor in curr_vert.get_neighbors():
            if neighbor.id not in visited:
                # print("Visited Before:", visited, neighbor.id)
                self._dfs_recursive(neighbor.id, to_vert, visited)
                # print("Visited After:", visited)
        return visited

    def _dfs_recursive_find_path(self, from_vert: str, to_vert: str):
        """
            Find a path between two vertices using DFS.
            Wraps the dfs algorithm to modify output
            Args:
            * from_vert - The from vertex to search from
            * to_vert - The to vertex to search to.
            Returns:
            The path we're between two vertices if they're found, None otherwise.
        """
        path = self._dfs_recursive(from_vert, to_vert, set())

        return path