from collections import deque

from graphs.utils import backtrace_path


class UnweightedGraph:
    def __init__(self):
        self.nodes = set()
        self.edges = set()
        self.adj = {}

    def __len__(self):
        return len(self.nodes)

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes.add(node)
            self.adj[node] = set()

    def add_multiple_nodes(self, nodes):
        for node in nodes:
            self.add_node(node)

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
                    return backtrace_path(start, end, parents)
                queue.append(next_node)

        return None
