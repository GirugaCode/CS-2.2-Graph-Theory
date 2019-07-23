#!python3
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
        #  return the neighbors
        return self.neighbors

    def get_id(self):
        """return the id of this vertex"""
        return self.id
        
class Graph:
    def __init__(self):
        """ 
        Initializes a graph object with an empty dictionary.
        self.vert_list -> List of the edges
        self.num_verticies -> List of verticies
        """
        # These represents the edges
        # self.vert_list = edges
        # self.num_verticies = verticies
        self.vert_list = {}
        self.num_verticies = 0

    def __repr__(self):
        return "<Test a:%s b:%s>" % (self.vert_list, self.num_verticies)

    def add_vertex(self, key):
        """
        Add a new vertex object to the graph with 
        the given key and return the vertex. 
        """
        self.num_verticies += 1
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex
        return new_vertex

    def add_edge(self, f, t, cost=0):
        """add an edge from vertex f to vertex t with a cost"""
        if f not in self.vert_list:
            self.add_vertex(f)
        if t not in self.vert_list:
            self.add_vertex(t)
        self.vert_list[f].add_neighbor(self.vert_list[t], cost)

    def get_vertices(self):
        """return all the vertices in the graph"""
        return self.vert_list.keys()

    def _bfs(self, from_vertex, to_vertex, visited=False):
        # Start with an arbitrary vertex
        # mark as visited and add to queue
        queue = []
        for vertex in queue:
            queue.pop(vertex)
            for neighbor in self.vert_list[vertex].neighbors:
                if not visited:
                    self.vert_list[vertex].neighbors = vertex
                    visited = True
        queue.append(neighbor)
        # For each vertex v in queue
        #     Remove v from the queue
        #     For each vertex u adjacent to v
        #         If u has not been visited
        #             Set parent of u to v
        #             Mark u as visited
        # Add u to the queue 

    def __iter__(self):
        """iterate over the vertex objects in the
        graph, to use sytax: for v in g
        """
        return iter(self.vert_list.values())

            


def main(text_file):
    '''
    Generate a graph from a file
    text_file -> name of file to open with graph data
    '''
    verticies_list = []
    edge_list = []
    graph = Graph()
    # Opens and Parses through the text file to set up Graph
    with open(text_file, "r") as open_file:
        line_counter = 0
        for line in open_file:
            if line_counter == 1:
                for key in line.strip().split(","):
                    verticies_list.append(key)
            elif line_counter > 1:
                edge = line.strip("()\n").split(",")
                if len(edge) > 3:
                    raise ValueError("The text file has to many arguments for the edges.")
                edge_list.append(edge)
            line_counter += 1

        # Adds all the vertexes to Graph
        for vertex in verticies_list:
            graph.add_vertex(vertex)

        # Adds all undirectional edges to Graph
        for edge in edge_list:
            graph.add_edge(edge[0], edge[1]) 
            graph.add_edge(edge[1], edge[0])

    print("Verticies:", list(graph.get_vertices()))
    
    # Prints all the Edges
    for key in graph:
        for value in key.get_neighbors():
            print(f"Edge:({key.get_id()}, {value.get_id()})")

    return graph


import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a graph from text files")
    parser.add_argument("filename", help="The name of the file to read from")
    # parser.add_argument("from_vertex", help="The from vertex you want to start at")
    # parser.add_argument("to_vertex", help="The to vertex you want to end at")
    args = parser.parse_args()

    if not args.filename:
        raise Exception("You didn't provide a file argument!")
    main(args.filename)



