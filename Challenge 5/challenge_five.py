#!python3
import argparse
from graphs.graph import Graph
from challenge_five_utils.read_file import read_file
            
def main(text_file):
    '''
    Generate a graph from a file
    text_file -> name of file to open with graph data
    '''
    graph, verts, edges = read_file(text_file)

    # Adds all the vertexes to Graph
    for vertex in verts:
        graph.add_vertex(vertex)

    # Adds all undirectional edges to Graph
    for edge in edges:
        graph.add_edge(edge[0], edge[1]) 

    print(f"This graph is Eulerian: {graph.is_eulerian()}")
    return graph

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a graph from text files")
    parser.add_argument("filename", help="The name of the file to read from")
    args = parser.parse_args()

    if not args.filename:
        raise Exception("You didn't provide a file argument!")
    main(args.filename)



