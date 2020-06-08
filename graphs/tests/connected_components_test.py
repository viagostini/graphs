from graphs.graph import Graph
from graphs.algorithms.connectivity import connected_components


def test_connected_components_single():
    graph = Graph(directed=False)
    graph.add_multiple_edges([(1, 2), (1, 3), (4, 2), (4, 5), (6, 4), (6, 7)])
    components = list(connected_components(graph))
    assert components == [{1, 2, 3, 4, 5, 6, 7}]


def test_connected_components_multiple():
    graph = Graph(directed=False)
    graph.add_multiple_edges([(1, 2), (1, 3), (4, 5), (6, 7)])
    components = list(connected_components(graph))
    assert components == [{1, 2, 3}, {4, 5}, {6, 7}]
