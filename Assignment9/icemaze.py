"""
CSCI-603 IceMaze Lab 9
file: hashmap.py
description: This program is an implementation of a frozen pond through which we need
to find the quickest way to escape from every possible row,column
author: Rishabh Arora, ra8851@rit.edu
author: Karan Ahluwalia,ka7982@rit.edu
"""
import sys

from graph import Graph


def main():
    """
    driver function, starts the program by taking arguments,reading file
    and find the shortest path
    :return:
    """
    filename = get_arguments()
    height, width, escape_row, graph = read_file(filename)
    # ESCAPE VERTEX
    escape_vertex = graph.getVertex((width - 1, escape_row))
    shortest_path(height, width, graph, escape_vertex)


def get_arguments():
    """"
    argument for taking the file name
    """
    if len(sys.argv) < 2:
        print("Usage: python3 icemaze.py {words-filename}")
        sys.exit()
    else:
        return sys.argv[1]


def read_file(filename):
    """
    reads the file provided in arguments
    :param filename: filename
    :return: multiple arguments
    """
    with open(filename) as file:
        props = file.readline().split()
        height = int(props[0])
        width = int(props[1])
        escape_row = int(props[2])
        pond = []
        for line in file:
            pond.append(line.split())
        graph = construct_graph(pond, height, width)
        return height, width, escape_row, graph


def construct_graph(pond, height, width):
    """
    construct graph using row,column from the pond
    :param pond: list of arrays read from the file
    :param height: height of the pond
    :param width: width of the pond
    :return: graph object
    """
    graph = Graph()
    for y in range(height):
        for x in range(width):
            if pond[y][x] == "*":
                continue
            else:
                vert = graph.addVertex((x, y)) if graph.getVertex((x, y)) is None else graph.getVertex((x, y))
            add_neighbours(pond, x, y, height, width, vert, graph)
    return graph


def add_neighbours(pond, x, y, height, width, vertex, graph):
    """
    add neighbours for every tuple of row and column
    """
    # column down
    counter = y
    while 0 <= counter < height and pond[counter][x] == '.':
        counter += 1
    if counter - 1 >= 0 and (x, counter - 1) != (x, y):
        graph.addEdge(vertex.id, (x, counter - 1))

    # column up
    counter = y
    while 0 <= counter < height and pond[counter][x] == '.':
        counter -= 1
    if counter + 1 >= 0 and (x, counter + 1) != (x, y):
        graph.addEdge(vertex.id, (x, counter + 1))

    # row right
    counter = x
    while 0 <= counter < width and pond[y][counter] == '.':
        counter += 1
    if counter - 1 >= 0 and (counter - 1, y) != (x, y):
        graph.addEdge(vertex.id, (counter - 1, y))

    # row left
    counter = x
    while 0 <= counter < width and pond[y][counter] == '.':
        counter -= 1
    if counter + 1 >= 0 and (counter + 1, y) != (x, y):
        graph.addEdge(vertex.id, (counter + 1, y))


def shortest_path(height, width, graph, escape_vertex):
    """
    find the shortest path between the escape node and the other nodes
    :param escape_vertex: defined in the file used to represent through which a node can escape
    :return: None
    """
    path_length_dict = {}
    no_path_list = []
    for y in range(height):
        for x in range(width):
            if (x, y) in graph.vertList:
                path = graph.findShortestPath(graph.getVertex((x, y)), escape_vertex)
                if path is not None:
                    if (x, y) == escape_vertex.id:
                        length = len(path)
                    else:
                        length = len(path) - 1
                    if length in path_length_dict:
                        path_length_dict[length].append((x, y))
                    else:
                        path_length_dict[length] = [(x, y)]
                else:
                    no_path_list.append((x, y))
    sort_and_print(path_length_dict, no_path_list)


def sort_and_print(path_length_dict, no_path_list):
    """
    sort the dictionary and print
    :param path_length_dict:
    :param no_path_list:
    :return:
    """
    sorted_list = []
    for key in path_length_dict:
        sorted_list.append((key, path_length_dict[key]))
        sorted_list = sorted(sorted_list)
    for length, coordinates in sorted_list:
        print(str(length) + ": " + str(coordinates))
    if len(no_path_list) > 0:
        print("No path: " + str(no_path_list))


if __name__ == '__main__':
    main()
