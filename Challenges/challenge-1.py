#!python3

class Graph:
    def __init__(self, verticies, edges):
        self.verticies = verticies
        self.edges = edges
        # self.weight = weight
    def __str__(self):

        return "Vertices: {} \nEdges: {}".format(self.verticies, self.edges)

    # def __repr__(self):
    #     return "Vertices: %s\nEdges: %s" % (len(self.verticies), len(self.edges))

    def _edges_weight(self):
        # ['(1,2,10)', '(1,4,20)', '(2,3,50)', '(2,4,11)']

        # weights = {
        #     (0, 2): 4,
        #     (0, 4): 60,
        #     (0, 3): 23,
        #     (2, 3): 4,
        #     (3, 1): 10,
        #     (4, 2): 15,
        # }
        edges_with_weight = self.edges
        print(edges_with_weight)
        




def graph_text(text_file):
    with open(text_file, "r") as open_file:
        text = open_file.read()
        clean_text = text.split("\n")
        
        graph = Graph(clean_text[1].split(","), clean_text[2:])
        print(graph._edges_weight())
        # return Graph(clean_text[1].split(","), clean_text[2:])

print(graph_text("graph-data.txt"))



