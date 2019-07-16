#!python3
class Vertex(object):
    def __init__(self, vertex):
        self.id = vertex
        self.neighbors = {}
        
class Graph:
    def __init__(self, verticies, edges):
        """ initializes a graph object with an empty dictionary."""
        # These represents the edges
        self.edge_list = edges
        self.num_verticies = verticies
    
    # def __str__(self):

    #     return "# Vertices: {} \n# Edges: {} \nEdge List:\n{}".format(len(self.num_verticies), len(self.edge_list), self.get_edges())

    # def get_edges(self):
    #     return self.edge_list

def main(text_file):
    verts = []
    edges = []
    graph = Graph(verts, edges)
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
        # text = open_file.read()
        # clean_text = text.split("\n")
        
        # graph = Graph(clean_text[1].split(","), [edge.strip('()').split(',') for edge in clean_text[2:]])
        # print(graph._edges_weight())
        # print([edge.strip('()').split(',') for edge in clean_text[2:]])
        print("# Verticies:", len(graph.edge_list))
        print("# Edges:", len(graph.num_verticies))
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



