#!python3
import argparse
from graphs.graph import Graph
from utils.read_file import read_file


def main(text_file):
    '''
    Generate a graph from a file
    text_file -> name of file to open with graph data
    '''

    graph, verts, edges = read_file(text_file)

    print("# Verticies:", len(verts))
    print("# Edges:", len(edges))
    # Iterates through the edge list and set all the edges with weights
    for fromVert, toVert, weight in edges:
        print(f"({fromVert}, {toVert}, {weight})")

    return graph





if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a graph from text files")
    parser.add_argument("filename", help="The name of the file to read from")
    args = parser.parse_args()

    if not args.filename:
        raise Exception("You didn't provide a file argument!")
    main(args.filename)



