#!python3

class Graph:
    def __init__(self, verticies, edges, weight):
        self.verticies = verticies
        self.edges = edges
        self.weight = weight
    
    def read_text(self, textfile):
        file = open("graph.txt", "r")
        return file

    print(read_text)