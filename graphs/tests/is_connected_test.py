from graphs.graph import Graph
from graphs.algorithms.connectivity import is_connected


def test_is_connected_true():
    graph = Graph(directed=False)
    graph.add_multiple_edges([(1, 2), (2, 3), (3, 4)])
    assert is_connected(graph)


def test_is_connected_false():
    graph = Graph(directed=False)
    graph.add_node(1)
    graph.add_multiple_edges([(2, 3), (3, 4)])
    assert not is_connected(graph)