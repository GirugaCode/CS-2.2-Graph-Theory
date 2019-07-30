#!python3
from data_structures.queue import LinkedQueue
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
        dict_edges = self.vert_dict[vertex].neighbors
        return dict_edges

    def _bfs(self, start_vertex):
        # Store the all visited verticies in a set
        visited = set()
        # Using Queues to traverse through the graph
        queue = LinkedQueue()
        queue.enqueue(start_vertex) # Start with enqueueing the starting vertex

        while not queue.is_empty(): # Loop as long as the queue contains verticies 
            vertex = queue.dequeue() # Dequeue the vertex
            for neighbor in self.vert_dict[vertex].neighbors: # Iterating through the dictionary of neighbors 
                if neighbor.id not in visited: # Check all neighbors if they are not visited
                    queue.enqueue(neighbor.id) # Enqueue the neighbors id that are not in visited
                    visited.add(neighbor.id) # Add the neighbor that is not in visited
        
        return visited

    def find_shortest_path(self, from_vert, to_vert):
        visited = set()
        vertex = self.vert_dict[from_vert]
        vertex.parent = None
        queue = LinkedQueue()
        queue.enqueue(vertex)
        visited.add(vertex.id)

        path_found = False

        while not queue.is_empty():
            vertex = queue.dequeue()
            if vertex.id == to_vert:
                path_found = True
                break

            for neighbor in vertex.neighbors:
                if neighbor.id not in visited:
                    queue.enqueue(neighbor)
                    visited.add(neighbor.id)
                    neighbor.parent = vertex

        if path_found:
            path = []
            while vertex:
                path.append(vertex.id)
                vertex = vertex.parent
            return path[::-1]

        

    def __iter__(self):
        """iterate over the vertex objects in the
        graph, to use sytax: for v in g
        """
        return iter(self.vert_dict.values())