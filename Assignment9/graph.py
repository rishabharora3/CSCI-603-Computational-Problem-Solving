"""
CSCI-603: Graphs
Author: Sean Strout @ RIT CS

An implementation of a graph data structure as an adjacency list.

Code taken from the online textbook and modified:

http://interactivepython.org/runestone/static/pythonds/Graphs/Implementation.html
"""

from vertex import Vertex


class Graph:
    """
    A graph implemented as an adjacency list of vertices.

    :slot: vertList (dict):  A dictionary that maps a vertex key to a Vertex
        object
    :slot: numVertices (int):  The total number of vertices in the graph
    """

    __slots__ = 'vertList', 'numVertices'

    def __init__(self):
        """
        Initialize the graph
        :return: None
        """
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        """
        Add a new vertex to the graph.
        :param key: The identifier for the vertex (typically a string)
        :return: Vertex
        """
        # count this vertex if not already present
        if self.getVertex(key) == None:
            self.numVertices += 1
            vertex = Vertex(key)
            self.vertList[key] = vertex
        return vertex

    def getVertex(self, key):
        """
        Retrieve the vertex from the graph.
        :param key: The vertex identifier
        :return: Vertex if it is present, otherwise None
        """
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None

    def __contains__(self, key):
        """
        Returns whether the vertex is in the graph or not.  This allows the
        user to do:

            key in graph

        :param key: The vertex identifier
        :return: True if the vertex is present, and False if not
        """
        return key in self.vertList

    def addEdge(self, src, dest, cost=0):
        """
        Add a new directed edge from a source to a destination of an edge cost.
        :param src: The source vertex identifier
        :param dest: The destination vertex identifier
        :param cost: The edge cost (defaults to 0)
        :return: None
        """
        if src not in self.vertList:
            self.addVertex(src)
        if dest not in self.vertList:
            self.addVertex(dest)
        self.vertList[src].addNeighbor(self.vertList[dest], cost)

    def getVertices(self):
        """
        Return the collection of vertex identifiers in the graph.
        :return: A list of vertex identifiers
        """
        return self.vertList.keys()

    def __iter__(self):
        """
        Return an iterator over the vertices in the graph.  This allows the
        user to do:

            for vertex in graph:
                ...

        :return: A list iterator over Vertex objects
        """
        return iter(self.vertList.values())

    def findShortestPath(self, start, end):
        """
        Find the shortest path, if one exists, between a start and end vertex
        :param start (Vertex): the start vertex
        :param end (Vertex): the destination vertex
        :return: A list of Vertex objects from start to end, if a path exists,
            otherwise None
        """
        # Using a queue as the dispenser type will result in a breadth first
        # search
        queue = []
        queue.append(start)  # prime the queue with the start vertex

        # The predecessor dictionary maps the current Vertex object to its
        # immediate predecessor.  This collection serves as both a visited
        # construct, as well as a way to find the path
        predecessors = {}
        predecessors[start] = None  # add the start vertex with no predecessor

        # Loop until either the queue is empty, or the end vertex is encountered
        while len(queue) > 0:
            current = queue.pop(0)
            if current == end:
                break
            for neighbor in current.getConnections():
                if neighbor not in predecessors:  # if neighbor unvisited
                    predecessors[neighbor] = current  # map neighbor to current
                    queue.append(neighbor)  # enqueue the neighbor

        # If the end vertex is in predecessors a path was found
        if end in predecessors:
            path = []
            current = end
            while current != start:  # loop backwards from end to start
                path.insert(0, current)  # prepend current to the path list
                current = predecessors[current]  # move to the predecessor
            path.insert(0, start)
            return path
        else:
            return None


def testGraph():
    """
    A test function for the Graph class.
    :return: None
    """
    STATES = {
        'CT': ('MA', 'RI'),
        'MA': ('CT', 'NH', 'RI', 'VT'),
        'ME': ('NH',),
        'NH': ('MA', 'ME', 'VT'),
        'RI': ('CT', 'MA'),
        'VT': ('MA', 'NH')
    }

    # add all the edges to the graph
    northeast = Graph()
    for state, neighbors in STATES.items():
        for neighbor in neighbors:
            # this automatically creates a new vertices if not already present
            northeast.addEdge(state, neighbor)

    # display the vertices, which will show the connected neighbors.
    # this will call the __iter__() method to get the Vertex objects.
    for state in northeast:
        print(state)

    print(northeast.getVertices())

    # check the __contains__() method
    print('MA in northeast (True)?', 'MA' in northeast)
    print('CA in northeast (False)?', 'CA' in northeast)

    # test getVertex()
    print('MA vertex:', northeast.getVertex('MA'))


if __name__ == '__main__':
    testGraph()
