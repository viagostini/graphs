"""
Class used to represent a Directed Graph.
"""

from graphs.base_graph import UnweightedGraph


class DirectedGraph(UnweightedGraph):

    def add_edge(self, from_node, to_node):
        self.add_multiple_nodes([from_node, to_node])

        self.adj[from_node].add(to_node)
        self.edges.add((from_node, to_node))

    def add_multiple_edges(self, edges):
        for from_node, to_node in edges:
            self.add_edge(from_node, to_node)


