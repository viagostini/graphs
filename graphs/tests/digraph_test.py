from graphs.digraph import DirectedGraph


def test_add_edge():
    digraph = DirectedGraph()
    digraph.add_edge(1, 2)
    digraph.add_edge(2, 4)
    assert digraph.adj == {1: {2}, 2: {4}, 4: set()}


def test_add_multiple_edges():
    digraph = DirectedGraph()
    digraph.add_multiple_edges([(1, 2), (2, 4), (2, 5)])
    assert digraph.adj == {1: {2}, 2: {4, 5}, 4: set(), 5: set()}


def test_shortest_path():
    graph = DirectedGraph()
    graph.add_multiple_edges([(1, 2), (2, 3), (3, 4), (4, 5), (2, 4)])
    assert graph.shortest_path(1, 4) == [1, 2, 4]
    assert graph.shortest_path(1, 6) is None
