"""
Class used to represent an Undirected Graph.
Also serves as a base class for directed graphs.
"""

from collections import defaultdict

class Graph:

    class Edge:
        """
        Internal class to represent an edge.
        """

        def __init__(self, from_node, to_node):
            """
            Initializes an Edge between two given nodes
            """
            self.from_node = from_node
            self.to_node = to_node

    def __init__(self):
        """
        Initializes an empty graph
        """
        self.nodes = set()
        self.edges = set()
        self.adj = defaultdict(set)

    def __len__(self):
        return len(self.nodes)

    def __contains__(self, node):
        return node in self.nodes

    def add_node(self, node):
        """
        Adds a new node to the graph
        """
        self.nodes.add(node)
        self.adj[node] = set()

    def add_edge(self, from_node, to_node):
        """
        Adds a new edge to the graph, also adding the nodes in case they aren't
        already in it
        """
        if from_node not in self:
            self.add_node(from_node)
        
        if to_node not in self:
            self.add_node(to_node)

        self.adj[from_node].add(to_node)
        self.adj[to_node].add(from_node)
        self.edges.add(self.Edge(from_node, to_node))
