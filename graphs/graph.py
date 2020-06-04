"""
Class used to represent an Undirected Graph.
Also serves as a base class for directed graphs.
"""

from collections import deque, defaultdict


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

    def add_node(self, node):
        """
        Adds a new node to the graph
        """
        self.nodes.add(node)
        self.adj[node] = set()

    def add_multiple_nodes(self, nodes):
        """
        Adds multiple nodes to the graph
        """
        for node in nodes:
            self.add_node(node)

    def add_edge(self, from_node, to_node):
        """
        Adds a new edge to the graph, also adding the nodes in case they aren't
        already in it
        """
        if from_node not in self.nodes:
            self.add_node(from_node)

        if to_node not in self.nodes:
            self.add_node(to_node)

        self.adj[from_node].add(to_node)
        self.adj[to_node].add(from_node)
        self.edges.add(self.Edge(from_node, to_node))

    def add_multiple_edges(self, edges):
        """
        Add multiple edges to the graph, adding the nodes in case they aren't
        already in it
        """
        for from_node, to_node in edges:
            self.add_edge(from_node, to_node)

    def is_connected(self):
        """
        Returns True if the graph is connected, False otherwise
        """
        visited = set()
        node = next(iter(self.nodes))
        self.depth_first_search(node, visited=visited)

        return True if len(visited) == len(self) else False

    def shortest_path(self, start, end):
        """
        Returns one (of the possibly many) shortest paths from start node
        to end node if one exists, None otherwise
        """
        parents = {}
        distances = {start: 0}

        queue = deque([start])
        while queue:
            node = queue.popleft()
            for next_node in (self.adj[node] - distances.keys()):
                parents[next_node] = node
                distances[next_node] = distances[node] + 1
                if next_node == end:
                    return self._backtrace_path(start, end, parents)
                queue.append(next_node)

        return None

    def _backtrace_path(self, start, end, parents):
        """
        Helper function to backtrace a path from parent information
        """
        path = deque([end])

        node = end
        while node != start:
            path.appendleft(parents[node])
            node = parents[node]

        return list(path)

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
