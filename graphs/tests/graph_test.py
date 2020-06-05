from graphs.graph import Graph


def test_initialization():
    graph = Graph()
    assert graph.adj == {}
    assert len(graph) == 0
    assert len(graph.nodes) == 0
    assert len(graph.edges) == 0


def test_add_node():
    graph = Graph()
    graph.add_node(1)
    graph.add_node(2)
    assert 1 in graph.nodes
    assert 2 in graph.nodes
    assert len(graph) == 2
    assert len(graph.nodes) == 2
    assert graph.adj == {1: set(), 2: set()}


def test_add_multiple_nodes():
    graph = Graph()
    graph.add_multiple_nodes((1, 2, 3, 4, 5))
    assert len(graph) == 5
    assert len(graph.nodes) == 5
    assert graph.adj == {1: set(), 2: set(), 3: set(), 4: set(), 5: set()}

    graph = Graph()
    graph.add_multiple_nodes([1, 2, 3, 4, 5])
    assert graph.adj == {1: set(), 2: set(), 3: set(), 4: set(), 5: set()}


def test_add_edge():
    graph = Graph()
    graph.add_node(1)
    graph.add_edge(1, 2)
    assert len(graph) == 2
    assert len(graph.nodes) == 2
    assert len(graph.edges) == 2
    assert (1, 2) in graph.edges
    assert (2, 1) in graph.edges
    assert graph.adj == {1: {2}, 2: {1}}


def test_add_multiple_edges():
    graph = Graph()
    graph.add_multiple_edges(((1, 2), (2, 3), (3, 4)))
    assert len(graph) == 4
    assert len(graph.edges) == 6
    assert graph.adj == {1: {2}, 2: {1, 3}, 3: {2, 4}, 4: {3}}

    graph = Graph()
    graph.add_multiple_edges([(1, 2), (2, 3), (3, 4)])
    assert graph.adj == {1: {2}, 2: {1, 3}, 3: {2, 4}, 4: {3}}


def test_is_connected():
    graph = Graph()
    graph.add_multiple_edges([(1, 2), (2, 3), (3, 4), (4, 5), (2, 4)])
    assert graph.is_connected()

    graph = Graph()
    graph.add_node(1)
    graph.add_multiple_edges([(2, 3), (3, 4), (4, 5), (2, 4)])
    assert not graph.is_connected()


def test_shortest_path():
    graph = Graph()
    graph.add_multiple_edges([(1, 2), (2, 3), (3, 4), (4, 5), (2, 4)])
    assert graph.shortest_path(1, 4) == [1, 2, 4]
    assert graph.shortest_path(1, 6) is None
