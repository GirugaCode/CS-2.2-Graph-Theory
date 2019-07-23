#!python3
from queue import LinkedQueue
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
        self.vert_list[t].add_neighbor(self.vert_list[f], cost)

    def get_vertices(self):
        """return all the vertices in the graph"""
        return self.vert_list.keys()

    def get_edges(self, vertex):
        dict_edges = self.vert_list[vertex].neighbors
        return dict_edges



    def _bfs(self, start_vertex):
        # Keep track of the visited verticies
        visited = set()
        # Keep track of the nodes queued to be checked
        queue = LinkedQueue()
        queue.enqueue(start_vertex)

        while not queue.is_empty():
            vertex = queue.dequeue()
            for neighbor in self.vert_list[vertex].neighbors:
                # print("Neighbor:", neighbor.id)
                if neighbor.id not in visited:
                    queue.enqueue(neighbor.id)
                    visited.add(neighbor.id)
        
        return visited

    def find_shortest_path(self, from_vert, to_vert):
        visited = set()
        vertex = self.vert_list[from_vert]
        vertex.parent = None
        queue = LinkedQueue()
        queue.enqueue(vertex)
        visited.add(vertex.id)

        path_found = False

        while not queue.is_empty():
            vertex = queue.dequeue()
            if vertex.id == to_vert:
                print('found')
                path_found = True
                break

            for neighbor in vertex.neighbors:
                if neighbor.id not in visited:
                    print(neighbor.id)
                    queue.enqueue(neighbor)
                    visited.add(neighbor.id)
                    neighbor.parent = vertex

        if path_found:
            path = []
            while vertex:
                path.append(vertex.id)
                vertex = vertex.parent
            print(path[::-1])   

        return visited

    def __iter__(self):
        """iterate over the vertex objects in the
        graph, to use sytax: for v in g
        """
        return iter(self.vert_list.values())

            
def main(text_file, from_vertex, to_vertex):
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
            # graph.add_edge(edge[1], edge[0])

    print("BFS:", graph._bfs("1"))
    graph.find_shortest_path(from_vertex, to_vertex)

    return graph


import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a graph from text files")
    parser.add_argument("filename", help="The name of the file to read from")
    parser.add_argument("from_vertex", help="The from vertex you want to start at")
    parser.add_argument("to_vertex", help="The to vertex you want to end at")
    args = parser.parse_args()

    if not args.filename:
        raise Exception("You didn't provide a file argument!")
    main(args.filename, args.from_vertex, args.to_vertex)



