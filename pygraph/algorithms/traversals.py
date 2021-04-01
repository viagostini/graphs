from distutils.util import execute
from typing import Hashable, List
from pygraph.graph import Graph


class DepthFirstSearch:
    def __init__(self, graph: Graph) -> None:
        self._graph = graph
        self.pre = {}
        self.post = {}
        self.parent = {}
        self._counter = 0

    def clear(self) -> None:
        self.pre, self.post, self.parent = {}, {}, {}

    @property
    def visited(self) -> set:
        return self.pre.keys()

    def execute(self, node: Hashable) -> None:
        self.pre[node] = self._counter
        self._counter += 1

        for next_node in self._graph.adjacency(node):
            if next_node not in self.visited:
                self.parent[next_node] = node
                self.execute(next_node)

        self.post[node] = self._counter
        self._counter += 1
