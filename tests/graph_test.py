import pytest

from pygraph.graph import Graph


def test_default_graph():
    """The default graph should be undirected, unweighted and be initialized empty"""
    graph = Graph()
    assert not len(graph)
    assert not graph.directed
    assert not graph.weighted


def test_add_node():
    graph = Graph()
    graph.add_node("São Paulo")
    graph.add_node("Rio de Janeiro")
    assert len(graph) == 2
    assert "São Paulo" in graph
    assert "Rio de Janeiro" in graph
    assert "Minas Gerais" not in graph


def test_add_undirected_edge():
    """
    When an edge (u, v) is added to an undirected Graph, the edge (v, u) is also added
    """
    graph = Graph(directed=False)
    graph.add_edge(1, 2)
    assert 2 in graph.adjacency(1)
    assert 1 in graph.adjacency(2)


def test_add_directed_edge():
    """
    When an edge (u, v) is added to a directed Graph, the edge (v, u) is not added
    """
    graph = Graph(directed=True)
    graph.add_edge(1, 2)
    assert 2 in graph.adjacency(1)
    assert 1 not in graph.adjacency(2)


def test_add_unweighted_edge():
    """A unweighted Graph only allows inserting unweighted edges """
    graph = Graph(weighted=False)
    graph.add_edge("São Paulo", "Rio de Janeiro", weight=None)

    with pytest.raises(RuntimeError):
        graph.add_edge("São Paulo", "Minas Gerais", weight=10)


def test_add_weighted_edge():
    """A weighted Graph only allows inserting weighted edges """
    graph = Graph(weighted=True)
    graph.add_edge("São Paulo", "Rio de Janeiro", weight=10)

    with pytest.raises(RuntimeError):
        graph.add_edge("São Paulo", "Minas Gerais", weight=None)