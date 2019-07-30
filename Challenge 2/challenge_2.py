#!python3
import argparse
from graphs.graph import Graph
from challenge_two_utils.read_file import read_file
            
def main(text_file, from_vertex, to_vertex):
    '''
    Generate a graph from a file
    text_file -> name of file to open with graph data
    '''
    # verticies_list = []
    # edge_list = []
    # graph = Graph()
    # # Opens and Parses through the text file to set up Graph
    # with open(text_file, "r") as open_file:
    #     line_counter = 0
    #     for line in open_file:
    #         if line_counter == 1:
    #             for key in line.strip().split(","):
    #                 verticies_list.append(key)
    #         elif line_counter > 1:
    #             edge = line.strip("()\n").split(",")
    #             if len(edge) > 3:
    #                 raise ValueError("The text file has to many arguments for the edges.")
    #             edge_list.append(edge)
    #         line_counter += 1

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

    # print("BFS:", graph._bfs("1"))
    short_path = graph.find_shortest_path(from_vertex, to_vertex)

    print(f"Verticies in shortest path: {short_path}")
    print(f"Number of edges in shortest path: {len(short_path) - 1}")

    return graph

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a graph from text files")
    parser.add_argument("filename", help="The name of the file to read from")
    parser.add_argument("from_vertex", help="The from vertex you want to start at")
    parser.add_argument("to_vertex", help="The to vertex you want to end at")
    args = parser.parse_args()

    if not args.filename:
        raise Exception("You didn't provide a file argument!")
    main(args.filename, args.from_vertex, args.to_vertex)



