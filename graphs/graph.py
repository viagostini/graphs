"""
Class used to represent an Undirected Graph.
Also serves as a base class for directed graphs.
"""

from collections import deque

from graphs.utils import backtrace_path
from graphs.base_graph import UnweightedGraph


class Graph(UnweightedGraph):

    def add_edge(self, node, other_node):
        """
        Adds a new edge to the graph, also adding the nodes in case they aren't
        already in it
        """
        self.add_multiple_nodes([node, other_node])

        self.adj[node].add(other_node)
        self.adj[other_node].add(node)
        self.edges.add((node, other_node))
        self.edges.add((other_node, node))

    def add_multiple_edges(self, edges):
        """
        Add multiple edges to the graph, adding the nodes in case they aren't
        already in it
        """
        for node, other_node in edges:
            self.add_edge(node, other_node)

    def is_connected(self):
        """
        Returns True if the graph is connected, False otherwise
        """
        visited = set()
        node = next(iter(self.nodes))
        self.depth_first_search(node, visited=visited)

        return True if len(visited) == len(self) else False

    def depth_first_search(self, node=None, visited=None):
        """
        Performs a depth-first traversal of the graph, marking nodes that
        have been seen in `visited`
        """
        if node is None:
            node = next(iter(self.nodes))

        if visited is None:
            visited = set()

        visited.add(node)
        for next_node in (self.adj[node] - visited):
            self.depth_first_search(next_node, visited)
