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
        
class Graph:
    def __init__(self, verticies, edges):
        """ 
        Initializes a graph object with an empty dictionary.
        self.edge_list -> List of the edges
        self.num_verticies -> List of verticies
        """
        # These represents the edges
        self.edge_list = edges
        self.num_verticies = verticies

def main(text_file):
    '''
    Generate a graph from a file
    text_file -> name of file to open with graph data
    '''
    verts = []
    edges = []
    graph = Graph(verts, edges)
    # Opens and Parses through the text file to set up Graph
    with open(text_file, "r") as open_file:
        line_counter = 0
        for line in open_file:
            if line_counter == 1:
                for key in line.strip().split(","):
                    verts.append(key)
            elif line_counter > 1:
                edge = line.strip("()\n").split(",")
                if len(edge) > 3:
                    raise ValueError("The text file has to many arguments for the edges.")
                edges.append(edge)
            line_counter += 1
        print("# Verticies:", len(graph.num_verticies))
        print("# Edges:", len(graph.edge_list))
        # Iterates through the edge list and set all the edges with weights
        for fromVert, toVert, weight in graph.edge_list:
            print(f"({fromVert}, {toVert}, {weight})")

        return graph


import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a graph from text files")
    parser.add_argument("filename", help="The name of the file to read from")
    args = parser.parse_args()

    if not args.filename:
        raise Exception("You didn't provide a file argument!")
    main(args.filename)



