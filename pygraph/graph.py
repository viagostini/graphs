from typing import Hashable, Iterator, Optional


class Graph:
    """Base class for all graphs. Represents an undirected, unweighted graph """

    def __init__(
        self,
        adjacency_dict: Optional[dict] = None,
        directed: Optional[bool] = None,
        weighted: Optional[bool] = None,
    ) -> None:

        if adjacency_dict and (directed is None or weighted is None):
            raise RuntimeError(
                "When building Graph from an adjacency dict, must pass `directed` and `weighted` arguments"
            )

        # we trust that it was called with proper directed and weighted arguments
        self.directed = directed or False
        self.weighted = weighted or False
        self._adj = adjacency_dict if adjacency_dict is not None else {}

    def __len__(self) -> int:
        return len(self._adj)

    def __contains__(self, key: Hashable) -> bool:
        return key in self._adj

    def __iter__(self) -> Iterator:
        return iter(self.nodes())

    def nodes(self) -> set:
        return set(self._adj.keys())

    def adjacency(self, node: Hashable) -> set:
        return self._adj[node]

    def add_node(self, key: Hashable) -> None:
        if key in self:
            raise RuntimeError("There is already a node with given key in Graph")
        self._adj[key] = set()

    def add_edge(
        self, node: Hashable, other: Hashable, weight: Optional[int] = None
    ) -> None:
        if weight and not self.weighted:
            raise RuntimeError("Trying to add a weighted edge on an unweighted graph")
        if not weight and self.weighted:
            raise RuntimeError("Trying to add an unweighted edge on a weighted graph")

        if weight:
            self._add_weighted_edge(node, other, weight)
        elif not weight:
            self._add_unweighted_edge(node, other)

    def _add_weighted_edge(self, node: Hashable, other: Hashable, weight: int) -> None:
        self._add_nodes_if_missing({node, other})
        self._adj[node].add((weight, other))
        if not self.directed:
            self._adj[other].add((weight, node))

    def _add_unweighted_edge(self, node: Hashable, other: Hashable) -> None:
        self._add_nodes_if_missing({node, other})
        self._adj[node].add(other)
        if not self.directed:
            self._adj[other].add(node)

    def _add_nodes_if_missing(self, nodes: set) -> None:
        for node in nodes - self.nodes():
            self.add_node(node)