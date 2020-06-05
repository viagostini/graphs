from graphs.graph import Graph
from graphs.algorithms.paths import bfs_shortest_path


def test_bfs_shortest_path_undirected():
    graph = Graph(directed=False)
    graph.add_multiple_edges([(1, 2), (2, 3), (3, 4), (4, 5), (4, 2)])
    assert bfs_shortest_path(graph, 1, 4) == [1, 2, 4]
    assert bfs_shortest_path(graph, 1, 6) is None


def test_bfs_shortest_path_directed():
    graph = Graph(directed=True)
    graph.add_multiple_edges([(1, 2), (2, 3), (3, 4), (4, 5), (4, 2)])
    assert bfs_shortest_path(graph, 1, 4) == [1, 2, 3, 4]
    assert bfs_shortest_path(graph, 1, 6) is None

