import pytest

from pygraph.decorators import expected_graph_types
from pygraph.graph import Graph


def test_expected_graph_types_undirected():
    @expected_graph_types(directed=False)
    def func(graph: Graph) -> bool:
        return True

    graph = Graph(directed=False)
    assert func(graph)

    graph = Graph(directed=True)
    with pytest.raises(RuntimeError):
        func(graph)


def test_expected_graph_types_directed():
    @expected_graph_types(directed=True)
    def func(graph: Graph) -> bool:
        return True

    graph = Graph(directed=True)
    assert func(graph)

    graph = Graph(directed=False)
    with pytest.raises(RuntimeError):
        func(graph)


def test_expected_graph_types_unweighted():
    @expected_graph_types(weighted=False)
    def func(graph: Graph) -> bool:
        return True

    graph = Graph(weighted=False)
    assert func(graph)

    graph = Graph(weighted=True)
    with pytest.raises(RuntimeError):
        func(graph)


def test_expected_graph_types_weighted():
    @expected_graph_types(weighted=True)
    def func(graph: Graph) -> bool:
        return True

    graph = Graph(weighted=True)
    assert func(graph)

    graph = Graph(weighted=False)
    with pytest.raises(RuntimeError):
        func(graph)