from pygraph.algorithms.traversals import DepthFirstSearch
from pygraph.graph import Graph


def test_depth_first_search():
    graph = Graph(
        {0: {1, 2, 3}, 1: {2, 4}, 2: set(), 3: set(), 4: {3}},
        directed=True,
        weighted=False,
    )

    dfs = DepthFirstSearch(graph)
    dfs.execute(0)
    assert dfs.visited == {0, 1, 2, 4, 3}


def test_depth_first_search():
    graph = Graph(
        {0: {1, 2}, 1: {2}, 2: set(), 3: {4}, 4: {3}},
        directed=True,
        weighted=False,
    )

    dfs = DepthFirstSearch(graph)
    dfs.execute(node=0)
    assert dfs.visited == {0, 1, 2}

    dfs.clear()
    dfs.execute(node=3)
    assert dfs.visited == {3, 4}
